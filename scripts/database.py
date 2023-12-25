import sqlcipher3
from scripts import consts

class Database(object):
    def __init__(self, password=None):
        self.db = sqlcipher3.connect(consts.__db_path__)
        self.cur = self.db.cursor()

        self.crypted_db = sqlcipher3.connect('./db/wallet.db')
        self.cr_cur = self.crypted_db.cursor()
        self.password = password

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
        self.cur.execute('select address from keys')
        r = self.cur.fetchall()
        for addr in r:
            addr_list.append(addr[0])
        return addr_list


