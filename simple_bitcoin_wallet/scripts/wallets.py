"""Некоторые функции для взаимодействия с сетью"""

from cryptos import *
from simple_bitcoin_wallet.scripts import consts
from simple_bitcoin_wallet.scripts.database import Database

__coin__ = Bitcoin(testnet=consts.__testnet__)

class GeneralFunctions(object):
    def __init__(self, password=None):
        self.password = password
        self.btc = __coin__
        self.DB = Database()


    def check_private_key(self, private_key):
        try:
            public_key = self.btc.privtopub(private_key)
            return public_key, self.btc.pubtoaddr(public_key)
            #self.ui.finish_import.clicked.connect(lambda: self.add_old_transactions_to_db(self.btc.pubtoaddr(public_key)))
        except:
            return False

    def add_transactions(self, addr=None):
        if addr is None:
            addr_list = self.DB.get_addresses_from_db()
        else:
            addr_list = [addr]
        history = self.btc.get_histories(*tuple(addr_list))
        for i in range(len(history)):
            tx_hash = history[i]['tx_hash']
            if self.DB.transaction_is_exists(tx_hash) is False and history[i]['height'] > 0:
                data = self.btc.inspect(self.btc.get_raw_tx(tx_hash))
                for y in data['ins']:
                    for x in data['outs']:
                        if y in addr_list:
                            sender = 'You'
                            type = 'output'
                            fee = data['fee']
                            if not x['address'] in addr_list:
                                recipient = x['address']
                                amount = x['value']
                        else:
                            type = 'input'
                            recipient = 'You'
                            if x['address'] in addr_list:
                                sender = y
                                amount = x['value']
                            fee = data['fee']
                self.DB.add_transaction_to_db(type, sender, recipient, tx_hash, amount, fee)

    def generate_new_address(self):
        mnemonic = Database(self.password).get_mnemonic()
        if mnemonic is None: # если кошелек недетерминированный - генерация новых адресов невозможна
            return False
        wallet = self.btc.wallet(mnemonic)

        new_address_index = self.DB.get_new_address_index()
        new_addr = wallet.receiving_address(new_address_index)
        priv_key = wallet.privkey(new_addr)
        public_key = self.btc.privtopub(wallet.privkey(new_addr))

        Database(self.password).insert_keys(priv_key, public_key, new_addr)
        return new_addr

    # Возвращает первый приватный ключ из первой пары ключей (с индексом 0)
    def get_first_private_key(self, mnemonic):
        wallet = self.btc.wallet(mnemonic)
        addr0 = wallet.receiving_address(0)
        priv_key = wallet.privkey(addr0)
        return priv_key
