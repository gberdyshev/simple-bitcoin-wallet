import sqlcipher3

from cryptos import *
from scripts import consts
from scripts.database import Database

__coin__ = Bitcoin(testnet=True)

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
                # если у нас есть адрес в ins, то транзакция типа "перевод OUT", если другой адрес "получение IN"
                for x in range(len(data['outs'])):
                    if next(iter(data['ins'])) in addr_list:
                        if not data['outs'][x]['address'] in addr_list:
                            recepient = data['outs'][x]['address']
                            sender = 'You'
                            type = 'output'
                            amount = data['outs'][x]['value']
                            fee = data['fee']
                            #self.DB.add_transaction_to_db(type, sender, recepient, tx_hash, amount, fee)
                    else:
                        if data['outs'][x]['address'] in addr_list:
                            type = 'input'
                            sender = next(iter(data['ins']))
                            recepient = 'You'
                            amount = data['outs'][x]['value']
                            fee = data['fee']
                self.DB.add_transaction_to_db(type, sender, recepient, tx_hash, amount, fee)

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

    def get_first_private_key(self, mnemonic):
        wallet = self.btc.wallet(mnemonic)
        addr0 = wallet.receiving_address(0)
        priv_key = wallet.privkey(addr0)
        return priv_key





   #def crypt_wallet_db(self):





class ImportWallet(object):
    def __init__(self):
        self.btc = __coin__





