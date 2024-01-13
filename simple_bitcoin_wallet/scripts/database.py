"""Работа с базой данных"""

import sqlite3 as sqlcipher3
import os

from simple_bitcoin_wallet.scripts import consts

class Database(object):
    def __init__(self, password=None):
        try:
            self.db = sqlcipher3.connect(consts.__db_path__)
            self.cur = self.db.cursor()

            self.crypted_db = sqlcipher3.connect(consts.__wallet_db_path__)
            self.cr_cur = self.crypted_db.cursor()
            self.password = password
        except:
    	    pass

    # Инициализация приложения: проверка существования файлов, создание таблиц в БД
    def init_app(self):
    
        if not os.path.exists(consts.__temp_path__):
            os.mkdir(consts.__temp_path__)
        if not os.path.exists(consts.__db_folder_path__):
            os.mkdir(consts.__db_folder_path__)
        db = sqlcipher3.connect(consts.__db_path__)
        cur = db.cursor()
        with open("simple_bitcoin_wallet/resources/init.sql", "r") as file:
            cur.executescript(file.read())
            db.commit()
        # проверка на наличие ключей
        cur.execute('select * from keys')
        r = cur.fetchone()
        if r is not None and os.path.exists(consts.__wallet_db_path__): # если ключи есть и есть файл с БД кошелька - вернуть истину
            return True


    # Возврат приватного ключа, соответствующего адресу
    def get_private_key(self, address):
        self.cr_cur.execute('PRAGMA KEY = "{}"'.format(self.password))
        self.cr_cur.execute("select private_key from keys where address = ?", (address,))
        r = self.cr_cur.fetchone()
        return r[0]

    # Проверка правильности пароля
    def check_password(self):
        try:
            self.cr_cur.execute('PRAGMA KEY = "{}"'.format(self.password))
            self.crypted_db.commit()
            self.cr_cur.execute('select private_key from keys')
            return True
        except:
            return False

    """
        Проверка, чтобы не генерировать новые адреса при непроведенных транзакциях,
        если адрес не был использован - можно использовать его (для сдачи)
    """
    def get_last_address(self):
        self.cur.execute("select address from keys")
        r = self.cur.fetchall()
        return r[-1][0] # возвращаем последний адрес

    # Получить список всех сгенерированных адресов из БД
    def get_addresses_from_db(self):
        addr_list = list()
        self.cur.execute("select address from keys")
        r = self.cur.fetchall()
        for addr in r:
            addr_list.append(addr[0])
        return addr_list

    # Получить индекс для нового адреса (Последний адрес: длина списка адресов - 1)
    def get_new_address_index(self):
        return len(self.get_addresses_from_db())

    # Проверка на детерминированность
    def walletIsDeterministic(self):
        f = False
        self.cr_cur.execute('PRAGMA KEY = "{}"'.format(self.password))
        self.cr_cur.execute("select mnemonic from mnemonic_keys")
        r = self.cr_cur.fetchone()
        if r[0] is not None: # если есть мнемоническая фраза - кошелек считается детерминированным, возвращаем истину
            f = True
        return f

    # Создание и шифрование wallet.db
    def crypt_wallet_db(self, private_key, public_key, address, mnemonic):
        self.cr_cur.execute('PRAGMA KEY = "{}"'.format(self.password))
        self.crypted_db.commit()
        self.cr_cur.execute("create table if not exists keys (private_key TEXT, public_key TEXT, address TEXT)")
        self.cr_cur.execute("create table if not exists mnemonic_keys (mnemonic TEXT)")
        self.cr_cur.execute('INSERT INTO keys (private_key, public_key, address) VALUES (?, ?, ?)',(private_key, public_key, address))
        self.cr_cur.execute('INSERT INTO mnemonic_keys (mnemonic) VALUES (?)',(mnemonic,))
        self.crypted_db.commit()

    # Добавление ключей в незашифрованную БД (открытый ключ и адрес)
    def add_keys_to_db(self, public_key, address):
        r = self.cur.execute('select * from keys where public_key = ?',(public_key,))
        if r.fetchone() is None:
            self.cur.execute('INSERT INTO keys (public_key, address) VALUES (?, ?)',(str(public_key), str(address)))
        self.db.commit()

    # Проверка существования транзакции
    def transaction_is_exists(self, tx_hash):
        self.cur.execute('select * from transactions where hash = ?', (tx_hash,))
        if self.cur.fetchone() is None:
            return False # транзакции нет
        else:
            return True

    # Добавление транзакции в data.db
    def add_transaction_to_db(self, type, sender, recipient, tx_hash, amount, fee):
        self.cur.execute('INSERT INTO transactions (type, sender, recipient, hash, amount, fee) VALUES (?, ?, ?, ?, ?, ?)',\
        (type, sender, recipient, tx_hash, amount, fee))
        self.db.commit()

    # Получить мнемоническую фразу из wallet.db
    def get_mnemonic(self):
        self.cr_cur.execute('PRAGMA KEY = "{}"'.format(self.password))
        self.cr_cur.execute("select mnemonic from mnemonic_keys")
        r = self.cr_cur.fetchone()
        if r[0] is not None:
            return r[0]

    # Вставка ключей в незашифрованную и зашифрованную БД
    def insert_keys(self, private_key, public_key, address):
        self.add_keys_to_db(public_key, address)
        self.cr_cur.execute('PRAGMA KEY = "{}"'.format(self.password))
        self.cr_cur.execute('INSERT INTO keys (private_key, public_key, address) VALUES (?, ?, ?)',(private_key, public_key, address))
        self.crypted_db.commit()

    # Получить приватный ключ (для кошельков вида пара ключей)
    def get_private_key_for_non_determ(self):
        self.cr_cur.execute('PRAGMA KEY = "{}"'.format(self.password))
        self.cr_cur.execute("select private_key from keys")
        r = self.cr_cur.fetchone()
        return r[0]

    def clean_transactions(self):
        self.cur.execute("delete from transactions")
        self.db.commit()
