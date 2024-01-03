# This Python file uses the following encoding: utf-8
import sys
import sqlcipher3
import requests
import qrcode
import os
import threading
import time
import random
import json

from ui import ui_form # Импорт основной формы
from ui import ui_firstrun_form as firstrun_form

from scripts.wallets import GeneralFunctions, Transaction
from scripts.tools import Tools
from scripts.database import Database
from scripts import consts

from cryptos import *
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget, QDialog, QTableWidgetItem, QInputDialog, QLineEdit
from PySide6.QtGui import QImage, QPixmap, QFont
from PySide6.QtCore import QThread

__db_folder_path__ = consts.__db_folder_path__
__db_path__ = consts.__db_path__
__wallet_db_path__ = consts.__wallet_db_path__ # Зашифрованная база для хранения секретного ключа
__temp_path__ = consts.__temp_path__
__coin__ = Bitcoin(testnet=True) # Какую монету используем, какую сеть
__currency__ = consts.__currency__ # если 10^8 - Биткоин, если 1 - сатоши (10^(-8) Биткоина)

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py





class MainWindow(QMainWindow):
    def __init__(self, parent=None, FirstRun=False, password=None):
        self.btc = __coin__
        super().__init__(parent)
        self.ui = ui_form.Ui_MainWindow()
        self.ui.setupUi(self)
        self.check_theme()
        self.ui.address_label.clicked.connect(lambda: QApplication.clipboard().setText(self.ui.address_label.text()))
        #if password is None:

        #if FirstRun is False:
            #password, ok = QInputDialog.getText(None, 'Аутентификация', 'Введите пароль:', QLineEdit.Password)
            #if Database(password).check_password() is False:
                #quit()
        self.ui.addresses_list.itemActivated.connect(self.address_item_change)
        self.ui.change_theme.clicked.connect(self.change_theme)
        self.ui.history_table.currentItemChanged.connect(lambda: self.get_transaction_inform(self.ui.history_table.item(self.ui.history_table.currentRow(),3).text()))
        self.ui.password_ok.clicked.connect(self.enter_to_wallet)
        self.password = password
        self.ui.pushButton.clicked.connect(self.send_transaction)
        self.ui.push_transaction.clicked.connect(lambda: self.send_tr(self.inputs, self.priv, self.inputs_summ, self.summ, self.new_addr))
        self.ui.pushButton_3.clicked.connect(self.dop)
        self.ui.contacts.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(7))

        #self.ui.hello.setText(f'Здравствуйте, {self.get_from_db("address")}')
        self.ui.setting.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(9))
        self.ui.get_mnemonic.clicked.connect(self.get_mnemonic)
        self.ui.show_bal.clicked.connect(lambda: threading.Thread(target=self.get_bal).start())
        #self.ui.show_bal.clicked.connect(lambda: self.ui.unconf_balance.setText(str('{0:.9f}'.format(self.get_bal('unconfirmed')))))
        self.ui.receive_button.clicked.connect(self.recieve)
        self.ui.history.clicked.connect(self.get_history)

        self.ui.load_button.clicked.connect(lambda: threading.Thread(target=self.update_history).start())
        self.ui.generate_new_addr.clicked.connect(lambda: self.generate_new_address())
        self.ui.go_to_home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.pushButton_2.clicked.connect(self.get_addresses)

    def enter_to_wallet(self):
        if Database(self.ui.password.text()).check_password():
            self.ui.stackedWidget.setCurrentIndex(0) # перейти на домашнюю страницу
            self.ui.menu_buttons.setEnabled(True)
            self.ui.pushButton_3.setEnabled(True)
            self.password = self.ui.password.text()
            threading.Thread(target=self.get_bal).start() # получаем и отображаем баланс
            self.cr_DB = Database(self.password)
            self.DB = Database()
            self.GenFunc = GeneralFunctions(self.password)
        else:
            QMessageBox.critical(self, 'Ошибка!', "Неверный пароль")


    def get_mnemonic(self):
        if self.ui.mnemonic.text() == "":
            QMessageBox.warning(self, 'Предупреждение!', "Никогда и никому не передавайте сид-фразу и секретные ключи от вашего кошелька!")
            if self.cr_DB.walletIsDeterministic() is False:
                text = self.cr_DB.get_private_key_for_non_determ()
            else:
                text = self.cr_DB.get_mnemonic()
            self.ui.mnemonic.setText(text)
        else:
            self.ui.mnemonic.setText("")



    def address_item_change(self, item):
        QApplication.clipboard().setText(item.text())


    def check_theme(self):
        theme = Tools().get_theme_option()
        if theme == "light":
            ui_style = consts.__ui_light_theme__
        elif theme == "dark":
            ui_style = consts.__ui_dark_theme__
        self.ui.centralwidget.setStyleSheet(ui_style)



    def change_theme(self):
        theme = Tools().get_theme_option()
        if theme == "light":
            ui_style = consts.__ui_dark_theme__
            theme_opt = "dark"
        elif theme == "dark":
            ui_style = consts.__ui_light_theme__
            theme_opt = "light"
        Tools().change_theme_option(theme_opt)
        self.ui.centralwidget.setStyleSheet(ui_style)


    def get_transaction_inform(self, hash):
        db = sqlcipher3.connect(__db_path__)
        cur = db.cursor()
        cur.execute("select * from transactions where hash = ?", (hash, ))
        r = cur.fetchone()
        if r[0] == 'input':
            self.ui.summ_2.setText(f"+ {str(r[4]/__currency__)}")
        else:
             self.ui.summ_2.setText(f"- {str(r[4]/__currency__)}")

        self.ui.hash_2.setText(r[3])

        self.ui.stackedWidget.setCurrentIndex(8)





    def update_history(self):
        FirstRunWindow().add_old_transactions_to_db()
        self.get_history()




    def get_history(self):


        self.ui.stackedWidget.setCurrentIndex(3)
        db = sqlcipher3.connect(__db_path__)
        cur = db.cursor()
        cur.execute('select * from transactions')
        r = cur.fetchall()
        self.ui.history_table.setRowCount(len(r)) # строчки
        #self.ui.history_table.setColumnCount(6)
        self.ui.history_table.setShowGrid(False)
        #self.ui.history_table.setHorizontalHeaderLabels(["Тип", "Отправитель", "Получатель","Хэш", "Сумма","Комиссия"])
        for i, (type, sender, recipient, hash, amount, fee) in enumerate(r):
            self.ui.history_table.setItem(i,0, QTableWidgetItem(type))
            self.ui.history_table.setItem(i,1, QTableWidgetItem(sender))
            self.ui.history_table.setItem(i,2, QTableWidgetItem(recipient))
            self.ui.history_table.setItem(i,3, QTableWidgetItem(hash))
            self.ui.history_table.setItem(i,4, QTableWidgetItem(str('{:.8f}'.format(amount/__currency__))))
            self.ui.history_table.setItem(i,5, QTableWidgetItem(str('{:.8f}'.format(fee/__currency__))))
        q = """select SUM(amount) from transactions where recepient = ?"""
        r = cur.execute(q, ("You",))
        r = r.fetchone()
        if r[0] is not None:
            self.ui.debet.setText(f'Всего поступило (дебет): {r[0]/__currency__}')
        q2 = """select SUM(amount) from transactions where sender = ?"""
        r = cur.execute(q2, ("You",))
        r = r.fetchone()
        if r[0] is not None:
            self.ui.credit.setText(f'Всего отправлено (кредит, без учёта комиссии): {r[0]/__currency__}')
        #self.ui.filter_history.addItems(["Все","Только отправка", "Только получение"])
        #self.ui.filter_history.currentTextChanged.connect(print('aa'))


    def get_addresses(self):
        r = self.DB.get_addresses_from_db()
        #self.ui.addresses_table.setRowCount(len(r)) # строчки
        #self.ui.addresses_table.setColumnCount(1)
        #self.ui.addresses_table.setHorizontalHeaderLabels(["Адрес"])
        self.ui.addresses_list.clear()
        for i, address in enumerate(r):
            self.ui.addresses_list.addItem(address)
            #self.ui.addresses_table.setItem(i,0, QTableWidgetItem(address))



    def generate_new_address(self):

        if Database(self.password).walletIsDeterministic() is False: # если кошелек недетерминированный - генерация новых адресов невозможна
            return QMessageBox.critical(self, 'Ошибка!', "Ваш кошелек является недетерминированным!")
        new_addr = self.GenFunc.generate_new_address()
        QApplication.clipboard().setText(new_addr)
        self.recieve()








    def recieve(self):
        self.ui.stackedWidget.setCurrentIndex(1) # открытие страницы
        address = Database().get_last_address()
        self.ui.address_label.setText(address)
        path = Tools().qrcode_generator(address)
        pixmap = QPixmap(path).scaled(200,200)
        self.ui.address_qr.setPixmap(pixmap)





    def get_bal(self):
        addresses = Database().get_addresses_from_db()
        bal = self.btc.get_balances(*tuple(addresses))
        confirmed_bal = unconfirmed_bal = 0
        for i in bal:
            confirmed_bal += i['confirmed']
            unconfirmed_bal += i['unconfirmed']
        #unconfirmed_bal = sum(i['unconfirmed'] for i in bal)
        self.ui.balance.setText(str(confirmed_bal/__currency__))
        self.ui.unconf_balance.setText(str(unconfirmed_bal/__currency__))
        #return bal/__currency__

        #return self.btc.get_balance(self.get_from_db('address'))[status]/__currency__


    def get_from_db(self, pos):
        db = sqlcipher3.connect(__db_path__)
        cur = db.cursor()
        cur.execute(f'select {pos} from keys')
        r = cur.fetchone()[0]
        return r




    def dop(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        #self.ui.pushButton.clicked.connect(self.send_transaction)
        #self.ui.pushButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(5))
        #self.ui.push_transaction.clicked.connect(lambda: self.send_tr(self.inputs, self.priv, self.inputs_summ, self.summ, self.new_addr))



    def send_tr(self, inputs, priv, inputs_summ, summ, new_addr):
        summ = int(float(self.ui.summ_recipient.text())*__currency__)
        outs = [{'value': summ, 'address': self.ui.address_recipient.text()}, {'value': inputs_summ -  summ - int(self.ui.comission_tr.text()), 'address': new_addr}]
        tx = self.btc.mktx(inputs, outs)
        password, ok = QInputDialog.getText(None, 'Подписание транзакции', 'Введите пароль:', QLineEdit.Password)
        check_password = Database(str(password)).check_password()
        if check_password is not False:
            tx2 = self.btc.signall(tx, priv)
            tx3 = serialize(tx2)
            tx_final = self.btc.pushtx(tx3)
            linkTemplate = '<a href={0}>{1}</a>'
            tx_link = f'https://testnet.bitcoinexplorer.org/tx/{tx_final}'
            self.ui.hash.setText(linkTemplate.format(tx_link, tx_final))
            self.ui.stackedWidget.setCurrentIndex(6)
            #db = sqlcipher3.connect(__db_path__)
            #cur = db.cursor()
            #cur.execute('INSERT INTO unconfirmed_transactions (type, sender, recepient, hash, amount, fee) VALUES (?, ?, ?, ?, ?, ?)', ('output', address,self.ui.addr.text() , tx_final, summ, 0))
            #db.commit()
        else:
            QMessageBox.critical(self, 'Ошибка!', "Неверный пароль")




    # Отправка транзакции
    def send_transaction(self):
        #try:
            #priv = self.get_from_db('private_key')
            #address = self.get_from_db('address')
            t = time.time()
            summ = round(float(self.ui.summ.text())*__currency__)
            db = sqlcipher3.connect(__wallet_db_path__)
            cur = db.cursor()
            cur.execute('PRAGMA KEY = "{}"'.format(self.password))
            cur.execute("select address, private_key from keys")
            r = cur.fetchall()
            #db1 = sqlcipher3.connect(__db_path__)
            #cur1 = db1.cursor()
            #cur1.execute('select address from keys')
            #r = cur1.fetchall()


            if self.btc.is_address(self.ui.addr.text()) is False:
                return QMessageBox.critical(self, 'Ошибка!', "Неверный адрес получателя")
            inputs_summ = 0
            all_in = []
            inputs = []
            priv_all_in = {}
            priv = {}
            for addr in r:
                all_in.append(addr[0])

            # формула расчета комисии: fee = (n_inputs * 148 + n_outputs * 34 + 10) * price_per_byte (где 10 - служебные доп данные)

            all_in = tuple(all_in)
            all_in = self.btc.get_unspents(*all_in)

            for unsp in all_in:
                if inputs_summ <= summ:
                    inputs.append(unsp)
                    addr = unsp['address']
                    priv[addr] = Database(self.password).get_private_key(addr)
                    inputs_summ += unsp['value']

            #fee = (len(inputs) * 148 + 2 * 34 + 10) * 1 # 2 - это выходы, пока они захардажены
            #print(inputs, priv)
            #print(inputs_summ)
            print(time.time()-t)
            last_address = Database(self.password).get_last_address()
            #print(Database(self.password).walletIsDeterministic())
            if len(self.btc.unspent(last_address)) == 0 or Database(self.password).walletIsDeterministic() is False:
                new_addr = last_address
            elif Database(self.password).walletIsDeterministic() is True:
                new_addr = self.GenFunc.generate_new_address()

            if inputs_summ - summ < 0 or summ <=0:
                return QMessageBox.critical(self, 'Ошибка!', "Недостаточно средств на счёте")

            #Сдача считается по формуле: входные данные - сумма отправки - комиссия


            def select_fee_option(value):
                fees = Tools().get_actual_fee()
                fee = 1
                if value == "Быстрая":
                    fee = fees[0]
                elif value == "Стандартная":
                    fee = fees[1]
                elif value == "Медленная":
                    fee = fees[2]
                fee_tr = Tools().calc_fee(len(inputs), 2, fee)
                self.ui.comission_byte.setText(str(fee))
                self.ui.comission_tr.setText(str(fee_tr))
                if inputs_summ - summ - fee_tr < 0:
                    return QMessageBox.critical(self, 'Ошибка!', "Недостаточно средств на счёте")


            def send_tr():
                print("а")
                #password = self.ui.password_2.text()
                summ = int(float(self.ui.summ_recipient.text())*__currency__)
                outs = [{'value': summ, 'address': self.ui.address_recipient.text()}, {'value': inputs_summ -  summ - int(self.ui.comission_tr.text()), 'address': new_addr}]
                tx = self.btc.mktx(inputs, outs)
                #QMessageBox.critical(self, 'Ошибка!', "Недостаточно средств на счёте")
                password, ok = QInputDialog.getText(None, 'Подписание транзакции', 'Введите пароль:', QLineEdit.Password)
                check_password = Database(str(password)).check_password()
                if check_password is not False:
                    tx2 = self.btc.signall(tx, priv)
                    tx3 = serialize(tx2)
                    tx_final = self.btc.pushtx(tx3)
                    linkTemplate = '<a href={0}>{1}</a>'
                    tx_link = f'https://testnet.bitcoinexplorer.org/tx/{tx_final}'
                    self.ui.hash.setText(linkTemplate.format(tx_link, tx_final))
                    self.ui.stackedWidget.setCurrentIndex(6)
                    #db = sqlcipher3.connect(__db_path__)
                    #cur = db.cursor()
                    #cur.execute('INSERT INTO unconfirmed_transactions (type, sender, recepient, hash, amount, fee) VALUES (?, ?, ?, ?, ?, ?)', ('output', address,self.ui.addr.text() , tx_final, summ, 0))
                    #db.commit()
                else:
                    QMessageBox.critical(self, 'Ошибка!', "Неверный пароль")
                #return 0

            self.ui.stackedWidget.setCurrentIndex(5)
            self.ui.address_recipient.setText(self.ui.addr.text())
            self.ui.summ_recipient.setText(self.ui.summ.text())
            self.ui.addr.setText("")
            self.ui.summ.setText("")
            self.ui.fee_options.setCurrentText("Выбор")
            self.ui.comission_byte.setText("")
            self.ui.comission_tr.setText("")

            #fees = Tools().get_actual_fee()
            self.ui.fee_options.currentTextChanged.connect(select_fee_option)
            self.inputs, self.priv, self.inputs_summ, self.summ, self.new_addr = inputs, priv, inputs_summ, summ, new_addr
            #self.ui.push_transaction.clicked.connect(lambda: self.send_tr(self.inputs, self.priv, self.inputs_summ, self.summ, self.new_addr))
            self.ui.cancel_transaction.clicked.connect(self.dop)
            #return 0
            #return inputs, priv, inputs_summ, summ, new_addr








        #except:
            #QMessageBox.critical(self, 'Ошибка!', "Проверьте корректность введенных данных")







class FirstRunWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = firstrun_form.Ui_MainWindow()
        self.btc = __coin__
        self.ui.setupUi(self)
        self.ui.create_wallet.clicked.connect(self.create_wallet)
        self.ui.import_wallet.clicked.connect(self.import_wallet)
        #self.ui.import_wallet_from_seed.clicked.connect(self.import_wallet_from_seed)


    #def import_wallet_from_seed(self):


    # Всё это в отдельные классы в отдельные файлы
    def import_wallet(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.mnemonic = False
        self.mnemonic_phrase = None
        self.ui.import_options.currentTextChanged.connect(self.select_option)
        #if self.ui.import_options.currentIndex() == 1:
            #print(0)
        self.ui.check.clicked.connect(self.check_keys)
        db = sqlcipher3.connect(__db_path__)
        cur = db.cursor()
        cur.execute("delete from transactions")
        db.commit()
        self.ui.finish_import_2.clicked.connect(lambda: self.add_password(self.ui.private_key_2.text(),self.ui.public_key_2.text(), self.ui.address_2.text(), self.mnemonic_phrase))

    def select_option(self, value):
        self.ui.private_key_2.setEnabled(False)
        self.ui.mnemonic_2.setEnabled(False)
        if value == "Секретный ключ":
            self.ui.private_key_2.setEnabled(True)
            self.mnemonic = False
        elif value == "Мнемоническая фраза":
            self.ui.mnemonic_2.setEnabled(True)
            self.mnemonic = True


        # !!!
    def add_old_transactions_to_db(self, addr=None):
        GeneralFunctions().add_transactions(addr)

        #value += int(100/len(history))
        self.ui.import_progress.setValue(100)
        print("б")
        self.ui.finish_import_2.setEnabled(True)
        #self.w2 = MainWindow()
        #self.ui.finish_import.clicked.connect(self.close())
        #self.ui.finish_import.clicked.connect(self.w2.show())



    def check_keys(self):
        try:
            if self.mnemonic is True:
                self.mnemonic_phrase = self.ui.mnemonic_2.text()
                self.ui.private_key_2.setText(GeneralFunctions().get_first_private_key(self.mnemonic_phrase))
            public_key, address = GeneralFunctions().check_private_key(self.ui.private_key_2.text())
            self.ui.public_key_2.setText(public_key)
            self.ui.address_2.setText(address)
            self.ui.finish_import.clicked.connect(lambda: self.add_old_transactions_to_db(address))
        except:
            QMessageBox.critical(self, 'Ошибка!', "Проверьте корректность секретного ключа или мнемонической фразы")

    def crypt_wdb(self, private_key, public_key, address, mnemonic):
        Database(self.ui.password.text()).crypt_wallet_db(private_key, public_key, address, mnemonic)
        Database().add_keys_to_db(public_key, address)


    def add_password(self,private_key, public_key, addr, mnemonic):
        self.ui.stackedWidget.setCurrentIndex(3)
        self.ui.confirm.clicked.connect(lambda: self.crypt_wdb(private_key, public_key, addr, mnemonic))








    def create_wallet(self):
        self.ui.stackedWidget.setCurrentIndex(2) # переход на сл страницу - создание кошелька
        self.ui.generate.clicked.connect(lambda: self.gen_keys()) # Вызывается gen_keys

        self.ui.go.setEnabled(True)
        self.ui.go.clicked.connect(lambda: self.add_password(self.ui.private_key.text(),self.ui.public_key.text() ,  self.ui.address.text(),self.ui.mnemonic.text()))


    def viewMnemonicAndPrivateKey(self):
        self.ui.private_key.setEchoMode(QLineEdit.EchoMode.Normal)
        self.ui.mnemonic.setEchoMode(QLineEdit.EchoMode.Normal)


    def gen_keys(self):
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
        #return self.generate_keys(private_key, public_key, addr)

        #self.ui.go.clicked.connect(lambda: self.add_keys_to_db(private_key, addr))












def init():
    if not os.path.exists(__temp_path__):
        os.mkdir(__temp_path__)
    if not os.path.exists(__db_folder_path__):
        os.mkdir(__db_folder_path__)
    db = sqlcipher3.connect(__db_path__)
    cur = db.cursor()
    cur.execute("create table if not exists keys (public_key TEXT, address TEXT)")
    cur.execute("create table if not exists transactions (type TEXT , sender TEXT, recepient TEXT, hash TEXT, amount INTEGER, fee INTEGER)")
    cur.execute("create table if not exists unconfirmed_transactions (type TEXT , sender TEXT, recepient TEXT, hash TEXT, amount INTEGER, fee INTEGER)")
    cur.execute("create table if not exists mnemonic_public_key (xpub_key TEXT)")
    db.commit()
    #wdb = sqlcipher3.connect(__wallet_db_path__)
    #wcur = wdb.cursor()
    #wcur.execute("create table if not exists keys (private_key TEXT, public_key TEXT, address TEXT)")
    #wdb.commit()

    cur.execute('select * from keys')
    if cur.fetchone() is not None: # если ключи есть и есть файл с БД кошелька - вернуть 1
        return 1

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.w1 = FirstRunWindow()
    def show_w1(self):

        self.w1 = FirstRunWindow()
        #self.w1.ui.go.clicked.connect(self.show_w2)
        #self.w1.ui.go.clicked.connect(self.w1.close)


        self.w1.ui.confirm.clicked.connect(self.show_w2)
        self.w1.ui.confirm.clicked.connect(self.w1.close)

        self.w1.show()

    def show_w2(self):
        self.w2 = MainWindow()
        self.w2.setFixedSize(1026, 533)
        self.w2.show()



if __name__ == "__main__":

    app = QApplication(sys.argv)
    widget = Main()
    #Main().hide()
    #widget.show()
    if init() == 1: # при наличии ключей запускается сразу MainWindow
        widget.show_w2()
    else:
        widget.show_w1() # при отсутствии ключей запускается мастер первоначальной настройки

    sys.exit(app.exec())
