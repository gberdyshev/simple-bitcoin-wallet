from cryptos import *
from scripts import consts

__coin__ = Bitcoin(testnet=True)

class GeneralFunctions(object):
    def __init__(self):
        self.btc = __coin__

    def check_private_key(self, private_key):
        try:
            public_key = self.btc.privtopub(private_key)
            return public_key, self.btc.pubtoaddr(public_key)
            #self.ui.finish_import.clicked.connect(lambda: self.add_old_transactions_to_db(self.btc.pubtoaddr(public_key)))
        except:
            return False

   #def crypt_wallet_db(self):





class ImportWallet(object):
    def __init__(self):
        self.btc = __coin__





