"""Класс и окно первоначальной настройки"""

import sqlcipher3
import os
import threading

# Импорт формы
from simple_bitcoin_wallet.ui import ui_firstrun_form as firstrun_form

# Импорт самописных функций
from simple_bitcoin_wallet.scripts.wallets import GeneralFunctions
from simple_bitcoin_wallet.scripts.database import Database
from simple_bitcoin_wallet.scripts import consts

from cryptos import *
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget, QDialog, QTableWidgetItem, QInputDialog, QLineEdit

__db_folder_path__ = consts.__db_folder_path__
__db_path__ = consts.__db_path__
__wallet_db_path__ = consts.__wallet_db_path__ # Зашифрованная база для хранения секретного ключа
__temp_path__ = consts.__temp_path__
__coin__ = Bitcoin(testnet=consts.__testnet__) # Какую монету используем, какую сеть
__currency__ = consts.__currency__ # если 10^8 - Биткоин, если 1 - сатоши (10^(-8) Биткоина)

class FirstRunWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = firstrun_form.Ui_MainWindow()
        self.btc = __coin__
        self.ui.setupUi(self)
        self.ui.create_wallet.clicked.connect(self.create_wallet)
        self.ui.import_wallet.clicked.connect(self.import_wallet)
    """ Добавление пароля """
    def add_password(self,private_key, public_key, addr, mnemonic):
        self.ui.stackedWidget.setCurrentIndex(3)
        self.ui.confirm.clicked.connect(lambda: self.crypt_wdb(
            private_key, 
            public_key, 
            addr, 
            mnemonic
            )) # Вызов функции шифрования базы данных

    """ Импорт кошелька """
    def import_wallet(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        Database().clean_transactions()
        self.mnemonic = False
        self.mnemonic_phrase = None
        self.ui.import_options.currentTextChanged.connect(self.select_option)
        self.ui.check.clicked.connect(self.check_keys)
        self.ui.finish_import_2.clicked.connect(lambda: self.add_password(
            self.ui.private_key_2.text(),
            self.ui.public_key_2.text(), 
            self.ui.address_2.text(), 
            self.mnemonic_phrase
            ))
    
    """ Выбор варианта импорта """
    def select_option(self, value):
        self.ui.private_key_2.setEnabled(False)
        self.ui.mnemonic_2.setEnabled(False)
        # Активация соответствующего поля в зависимости от варианта
        if value == "Секретный ключ":
            self.ui.private_key_2.setEnabled(True)
            self.mnemonic = False
        elif value == "Мнемоническая фраза":
            self.ui.mnemonic_2.setEnabled(True)
            self.mnemonic = True

    """ Добавление ранее имеющихся транзакций в БД """
    def add_old_transactions_to_db(self, *addr):
        self.ui.importer_frame_3.setEnabled(False)
        GeneralFunctions().add_transactions(addr[0])
        self.ui.import_progress.setValue(100)
        self.ui.finish_import_2.setEnabled(True)

    """ Проверка мнемонической фразы (секретного ключа) """
    def check_keys(self):
        try:
            if self.mnemonic is True:
                self.mnemonic_phrase = self.ui.mnemonic_2.text()
                self.ui.private_key_2.setText(GeneralFunctions().get_first_private_key(self.mnemonic_phrase))
            public_key, address = GeneralFunctions().check_private_key(self.ui.private_key_2.text())
            self.ui.public_key_2.setText(public_key)
            self.ui.address_2.setText(address)
            args = tuple([address])
            print(args)
            self.ui.finish_import.clicked.connect(lambda: threading.Thread(target=self.add_old_transactions_to_db, args=args).start())
        except:
            QMessageBox.critical(self, 'Ошибка!', "Проверьте корректность секретного ключа или мнемонической фразы")

    def crypt_wdb(self, private_key, public_key, address, mnemonic):
        Database(self.ui.password.text()).crypt_wallet_db(private_key, public_key, address, mnemonic)
        Database().add_keys_to_db(public_key, address)

    """ Создание кошелька """
    def create_wallet(self):
        self.ui.stackedWidget.setCurrentIndex(2) # переход на сл страницу - создание кошелька
        self.ui.generate.clicked.connect(lambda: self.gen_keys()) # Вызывается gen_keys

        self.ui.go.setEnabled(True)
        self.ui.go.clicked.connect(lambda: self.add_password(
            self.ui.private_key.text(),
            self.ui.public_key.text(),  
            self.ui.address.text(),
            self.ui.mnemonic.text()
            ))

    """ Показать мнемоническую фразу (секретный ключ) """
    def viewMnemonicAndPrivateKey(self):
        self.ui.private_key.setEchoMode(QLineEdit.EchoMode.Normal)
        self.ui.mnemonic.setEchoMode(QLineEdit.EchoMode.Normal)

    """ Генерация мнемонической фразы """
    def gen_keys(self):
        Database().clean_transactions() # Очистка базы данных от транзакций (если они есть)
        words = entropy_to_words(os.urandom(16))
        wallet = self.btc.wallet(words)
        addr = wallet.new_receiving_address()
        private_key = wallet.privkey(addr)
        public_key = self.btc.privtopub(private_key)
        self.ui.mnemonic.setText(words)
        self.ui.private_key.setText(private_key)
        self.ui.show_private_key.setEnabled(True)
        self.ui.public_key.setText(public_key)
        self.ui.address.setText(addr)
        self.ui.show_private_key.clicked.connect(lambda: self.viewMnemonicAndPrivateKey())