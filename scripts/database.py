import sqlcipher3
import os

from scripts import consts

class Database(object):
    def __init__(self, password=None):
        self.db = sqlcipher3.connect(consts.__db_path__)
        self.cur = self.db.cursor()

        self.crypted_db = sqlcipher3.connect(consts.__wallet_db_path__)
        self.cr_cur = self.crypted_db.cursor()
        self.password = password


    @property
    def _password(self):
        return self.password

    @_password.setter
    def _password(self, password):
        self.password = password

    # возврат приватного ключа, соответствующего адресу
    def get_private_key(self, address):
        self.cr_cur.execute('PRAGMA KEY = "{}"'.format(self.password))
        self.cr_cur.execute("select private_key from keys where address = ?", (address,))
        r = self.cr_cur.fetchone()
        return r[0]

    def check_password(self):
        try:
            self.cr_cur.execute('PRAGMA KEY = "{}"'.format(self.password))
            self.crypted_db.commit()
            self.cr_cur.execute('select private_key from keys')
            return True
        except:
            return False

    """Проверка, чтобы не генерировать новые адреса при непроведенных транзакциях,
    если адрес не был использован - можно использовать его (для сдачи)"""
    def get_last_address(self):
        self.cur.execute("select address from keys")
        r = self.cur.fetchall()
        return r[-1][0] # возвращаем последний адрес

    def get_addresses_from_db(self):
        addr_list = list()
        self.cur.execute("select address from keys")
        r = self.cur.fetchall()
        for addr in r:
            addr_list.append(addr[0])
        return addr_list

    # Проверка на детерминированность
    def walletIsDeterministic(self):
        f = False
        self.cr_cur.execute('PRAGMA KEY = "{}"'.format(self.password))
        self.cr_cur.execute("select mnemonic from mnemonic_keys")
        r = self.cr_cur.fetchone()
        if r[0] is not None: # если есть мнемоническая фраза - кошелек считается детерминированным, возвращаем истину
            f = True
        return f

    def crypt_wallet_db(self, private_key, public_key, address, mnemonic):
        self.cr_cur.execute('PRAGMA KEY = "{}"'.format(self.password))
        self.crypted_db.commit()
        self.cr_cur.execute("create table if not exists keys (private_key TEXT, public_key TEXT, address TEXT)")
        self.cr_cur.execute("create table if not exists mnemonic_keys (mnemonic TEXT)")
        self.cr_cur.execute('INSERT INTO keys (private_key, public_key, address) VALUES (?, ?, ?)',(private_key, public_key, address))
        self.cr_cur.execute('INSERT INTO mnemonic_keys (mnemonic) VALUES (?)',(mnemonic,))
        self.crypted_db.commit()

    def add_keys_to_db(self, public_key, address):
        r = self.cur.execute('select * from keys where public_key = ?',(public_key,))
        if r.fetchone() is None:
            self.cur.execute('INSERT INTO keys (public_key, address) VALUES (?, ?)',(str(public_key), str(address)))
        #cur.execute('INSERT INTO mnemonic_public_key (xpub_key) VALUES (?)',(xpub_key))
        self.db.commit()









