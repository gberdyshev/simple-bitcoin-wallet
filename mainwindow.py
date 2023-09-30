# This Python file uses the following encoding: utf-8
import sys
import ui_form # Импорт основной формы
import ui_firstrun_form as firstrun_form
import sqlcipher3
import requests
import qrcode
import os
import time
from cryptos import *
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget, QDialog, QTableWidgetItem, QInputDialog, QLineEdit
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QThread

__db_path__ = './db/data.db'
__wallet_db_path__ = './db/wallet.db' # Зашифрованная база для хранения секретного ключа
__temp_path__ = './.temp/'
__coin__ = Bitcoin(testnet=True) # Какую монету используем, какую сеть
__currency__ = 10**8 # если 10^8 - Биткоин, если 1 - сатоши (10^(-8) Биткоина)

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py




class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        self.btc = __coin__
        super().__init__(parent)
        self.ui = ui_form.Ui_MainWindow()
        self.ui.setupUi(self)
        #password, ok = QInputDialog.getText(None, 'Аутентификация', 'Введите пароль:', QLineEdit.Password)
        #if self.check_password(password) is False:
        #    quit()

        self.ui.pushButton.clicked.connect(self.send_transaction)
        self.ui.pushButton_3.clicked.connect(self.dop)
        #self.ui.hello.setText(f'Здравствуйте, {self.get_from_db("address")}')
        self.ui.show_bal.clicked.connect(lambda: self.ui.balance.setText(str(self.get_bal('confirmed'))))
        self.ui.show_bal.clicked.connect(lambda: self.ui.unconf_balance.setText(str('{0:.9f}'.format(self.get_bal('unconfirmed')))))
        self.ui.receive_button.clicked.connect(self.recieve)
        self.ui.history.clicked.connect(self.get_history)

    def check_password(self, password):
        try:
            db = sqlcipher3.connect(__wallet_db_path__)
            cur = db.cursor()
            cur.execute('PRAGMA KEY = "{}"'.format(password))
            db.commit()
            r = cur.execute('select private_key from keys')
            return r.fetchone()[0]
        except:
            return False




    def get_history(self):

        self.ui.stackedWidget.setCurrentIndex(3)
        db = sqlcipher3.connect(__db_path__)
        cur = db.cursor()
        cur.execute('select * from transactions')
        r = cur.fetchall()
        self.ui.history_table.setRowCount(len(r)) # строчки
        self.ui.history_table.setColumnCount(6)
        self.ui.history_table.setHorizontalHeaderLabels(["Тип", "Отправитель", "Получатель","Хэш", "Сумма","Комиссия"])
        for i, (type, sender, recipient, hash, amount, fee) in enumerate(r):
            self.ui.history_table.setItem(i,0, QTableWidgetItem(type))
            self.ui.history_table.setItem(i,1, QTableWidgetItem(sender))
            self.ui.history_table.setItem(i,2, QTableWidgetItem(recipient))
            self.ui.history_table.setItem(i,3, QTableWidgetItem(hash))
            self.ui.history_table.setItem(i,4, QTableWidgetItem(str('{:.8f}'.format(amount/__currency__))))
            self.ui.history_table.setItem(i,5, QTableWidgetItem(str('{:.8f}'.format(fee/__currency__))))
        q = """select SUM(amount) from transactions where recepient = ?"""
        r = cur.execute(q, (self.get_from_db('address'),))
        r = r.fetchone()
        if r[0] is not None:
            self.ui.debet.setText(f'Всего поступило (дебет): {r[0]/__currency__}')
        q2 = """select SUM(amount) from transactions where sender = ?"""
        r = cur.execute(q2, (self.get_from_db('address'),))
        r = r.fetchone()
        if r[0] is not None:
            self.ui.credit.setText(f'Всего отправлено (кредит, без учёта комиссии): {r[0]/__currency__}')

        #self.ui.filter_history.addItems(["Все","Только отправка", "Только получение"])
        #self.ui.filter_history.currentTextChanged.connect(print('aa'))




    def recieve(self): # !!!надо qr-код сделать!!!
        self.ui.stackedWidget.setCurrentIndex(1) # открытие страницы
        address = self.get_from_db('address')
        self.ui.address_label.setText(address)
        self.ui.address_label.clicked.connect(lambda: QApplication.clipboard().setText(address))
        img = qrcode.make(address)
        path = f"{__temp_path__}qr_{address}.png"
        img.save(path)
        pixmap = QPixmap(path).scaled(200,200)
        self.ui.address_qr.setPixmap(pixmap)




    # Расчёт комиссии, принимает аргумент: размер транзакции (в Байтах)
    def calc_fee(self, size):
        r = requests.get('https://api.blockcypher.com/v1/btc/test3')
        r = r.json()
        high = r['high_fee_per_kb']
        medium = r['medium_fee_per_kb']
        low = r['low_fee_per_kb']
        size_kb = size / 1024
        print(size_kb*low)


    def get_bal(self, status):
        return self.btc.get_balance(self.get_from_db('address'))[status]/__currency__


    def get_from_db(self, pos):
        db = sqlcipher3.connect(__db_path__)
        cur = db.cursor()
        cur.execute(f'select {pos} from keys')
        r = cur.fetchone()[0]
        return r

    def dop(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    # Отправка транзакции
    def send_transaction(self):
        #try:
            #priv = self.get_from_db('private_key')
            address = self.get_from_db('address')
            inputs = self.btc.unspent(address)
            summ = int(float(self.ui.summ.text())*10**8)
            #Сдача считается по формуле: входные данные - сумма отправки - комиссия
            if sum(i['value'] for i in inputs) - summ - 3177 < 0 or summ <=0:
                return QMessageBox.critical(self, 'Ошибка!', "Недостаточно средств на счёте")
            elif self.btc.is_address(self.ui.addr.text()) is False:
                return QMessageBox.critical(self, 'Ошибка!', "Неверный адрес получателя")
            outs = [{'value': summ, 'address': self.ui.addr.text()}, {'value': sum(i['value'] for i in inputs) -  summ - 3177, 'address': address}]
            tx = self.btc.mktx(inputs, outs)
            password, ok = QInputDialog.getText(None, 'Подписание транзакции', 'Введите пароль:', QLineEdit.Password)
            priv = self.check_password(str(password))
            if priv is not False:
                tx2 = self.btc.signall(tx, priv)
                tx3 = serialize(tx2)
                tx_final = self.btc.pushtx(tx3)
                linkTemplate = '<a href={0}>{1}</a>'
                tx_link = f'https://live.blockcypher.com/btc-testnet/tx/{tx_final}'
                self.ui.hash.setText(linkTemplate.format(tx_link, tx_final))
                db = sqlcipher3.connect(__db_path__)
                cur = db.cursor()
                cur.execute('INSERT INTO unconfirmed_transactions (type, sender, recepient, hash, amount, fee) VALUES (?, ?, ?, ?, ?, ?)', ('output', address,self.ui.addr.text() , tx_final, summ, 0))
                db.commit()
            else:
                QMessageBox.critical(self, 'Ошибка!', "Неверный пароль")

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


    # Всё это в отдельные классы в отдельные файлы
    def import_wallet(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.check.clicked.connect(self.check_keys)
        self.ui.finish_import_2.clicked.connect(lambda: self.add_password(self.ui.private_key_2.text(),self.ui.public_key_2.text(), self.ui.address_2.text()))

        # !!!
    def add_old_transactions_to_db(self, address):
        history = self.btc.get_histories(address)
        db = sqlcipher3.connect(__db_path__)
        value = self.ui.import_progress.value()
        cur = db.cursor()
        for i in range(len(history)):
            tx_hash = history[i]['tx_hash']
            if history[i]['height'] != 0:
                data = self.btc.inspect(self.btc.get_raw_tx(tx_hash))
                # если у нас есть адрес в ins, то транзакция типа "перевод OUT", если другой адрес "получение IN"
                for x in range(len(data['outs'])):
                    if next(iter(data['ins'])) == address:
                        if data['outs'][x]['address'] != address:
                            recepient = data['outs'][x]['address']
                            sender = address
                            type = 'output'
                            amount = data['outs'][x]['value']
                            fee = data['fee']
                            cur.execute('INSERT INTO transactions (type, sender, recepient, hash, amount, fee) VALUES (?, ?, ?, ?, ?, ?)', (type, sender, recepient, tx_hash, amount, fee))
                            #db.commit()
                    else:
                        if data['outs'][x]['address'] == address:
                            type = 'input'
                            sender = next(iter(data['ins']))
                            recepient = address
                            amount = data['outs'][x]['value']
                            fee = data['fee']
                            cur.execute('INSERT INTO transactions (type, sender, recepient, hash, amount, fee) VALUES (?, ?, ?, ?, ?, ?)', (type, sender, recepient, tx_hash, amount, fee))
                    db.commit()
                    self.ui.import_progress.setValue(value+int(100/len(history)))
                    value += int(100/len(history))
        self.ui.finish_import_2.setEnabled(True)
        #self.w2 = MainWindow()
        #self.ui.finish_import.clicked.connect(self.close())
        #self.ui.finish_import.clicked.connect(self.w2.show())



    def check_keys(self):
            #try:
        private_key = self.ui.private_key_2.text()
        public_key = self.btc.privtopub(private_key)
        self.ui.public_key_2.setText(public_key)
        self.ui.address_2.setText(self.btc.pubtoaddr(self.btc.privtopub(private_key)))
        self.ui.finish_import.clicked.connect(lambda: self.add_keys_to_db(public_key, self.btc.pubtoaddr(public_key)))
        self.ui.finish_import.clicked.connect(lambda: self.add_old_transactions_to_db(self.btc.pubtoaddr(public_key)))
            #except:
                #QMessageBox.critical(self, 'Ошибка!', "Проверьте корректность секретного ключа")

    def crypt_wdb(self, private_key, public_key, address):

        wdb = sqlcipher3.connect(__wallet_db_path__)
        cur = wdb.cursor()
        cur.execute('PRAGMA KEY = "{}"'.format(self.ui.password.text()))
        wdb.commit()
        cur.execute("create table if not exists keys (private_key TEXT, public_key TEXT, address TEXT)")
        cur.execute('INSERT INTO keys (private_key, public_key, address) VALUES (?, ?, ?)',(private_key, public_key, address))
        wdb.commit()
        print('a')


    def add_password(self,private_key, public_key, addr):
        self.ui.stackedWidget.setCurrentIndex(3)
        self.ui.confirm.clicked.connect(lambda: self.crypt_wdb(private_key, public_key, addr))








    def create_wallet(self):
        self.ui.stackedWidget.setCurrentIndex(2) # переход на сл страницу - создание кошелька
        self.ui.generate.clicked.connect(lambda: self.gen_keys()) # Вызывается gen_keys

        self.ui.go.setEnabled(True)
        self.ui.go.clicked.connect(lambda: self.add_keys_to_db(self.ui.public_key.text() ,  self.ui.address.text()))
        self.ui.go.clicked.connect(lambda: self.add_password(self.ui.private_key.text(),self.ui.public_key.text() ,  self.ui.address.text()))



    def gen_keys(self):
        private_key = random_key()
        public_key = self.btc.privtopub(private_key)
        addr = self.btc.pubtoaddr(public_key)
        self.ui.private_key.setText(private_key)
        self.ui.show_private_key.setEnabled(True)
        self.ui.public_key.setText(public_key)
        self.ui.address.setText(addr)
        self.ui.show_private_key.clicked.connect(lambda: self.ui.private_key.setEchoMode(QLineEdit.EchoMode.Normal))
        #return self.generate_keys(private_key, public_key, addr)

        #self.ui.go.clicked.connect(lambda: self.add_keys_to_db(private_key, addr))




    # Функция добавления ключей в БД
    def add_keys_to_db(self, public_key, addr):
        db = sqlcipher3.connect(__db_path__)
        cur = db.cursor()
        cur.execute('INSERT INTO keys (public_key, address) VALUES (?, ?)',(str(public_key), str(addr)))
        db.commit()





def init():
    if not os.path.exists(__temp_path__):
        os.mkdir(__temp_path__)
    db = sqlcipher3.connect(__db_path__)
    cur = db.cursor()
    cur.execute("create table if not exists keys (public_key TEXT, address TEXT)")
    cur.execute("create table if not exists transactions (type TEXT , sender TEXT, recepient TEXT, hash TEXT, amount INTEGER, fee INTEGER)")
    cur.execute("create table if not exists unconfirmed_transactions (type TEXT , sender TEXT, recepient TEXT, hash TEXT, amount INTEGER, fee INTEGER)")
    db.commit()

    #wdb = sqlcipher3.connect(__wallet_db_path__)
    #wcur = wdb.cursor()
    #wcur.execute("create table if not exists keys (private_key TEXT, public_key TEXT, address TEXT)")
    #wdb.commit()

    cur.execute('select * from keys')
    if cur.fetchone() is not None: # если ключи есть - вернуть 1
        return 1

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
    def show_w1(self):

        self.w1 = FirstRunWindow()
        #self.w1.ui.go.clicked.connect(self.show_w2)
        #self.w1.ui.go.clicked.connect(self.w1.close)


        self.w1.ui.confirm.clicked.connect(self.show_w2)
        self.w1.ui.confirm.clicked.connect(self.w1.close)

        self.w1.show()

    def show_w2(self):
        self.w2 = MainWindow()
        self.w2.show()



if __name__ == "__main__":

    app = QApplication(sys.argv)
    widget = Main()
    Main().hide()
    widget.show()
    if init() == 1: # при наличии ключей запускается сразу MainWindow
        widget.show_w2()
    else:
        widget.show_w1() # при отсутствии ключей запускается мастер первоначальной настройки


    sys.exit(app.exec())
