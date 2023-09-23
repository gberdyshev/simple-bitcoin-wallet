# This Python file uses the following encoding: utf-8
import sys
import ui_form # Импорт основной формы
import firstrun_form
import sqlite3
import time
from cryptos import *
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget, QDialog
from PySide6 import QtSql

__db_path__ = './wallet.db'
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        self.btc = Bitcoin(testnet=True)

        super().__init__(parent)
        self.ui = ui_form.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.send_transaction)
        self.ui.pushButton_3.clicked.connect(self.dop)
        self.ui.hello.setText(f'Здравствуйте, {self.get_from_db("address")}')
        self.ui.show_bal.clicked.connect(lambda: self.ui.balance.setText(str(self.get_bal())))

        #self.ui.recieve_button.clicked.connect(self.recieve)

    #def recieve(self)


    def get_bal(self):
        result = pow(10, 8//2) # Оптимизация возведения 10^8
        result = result * result
        if 8 % 2 != 0:
            result = result * val
        return self.btc.get_balance(self.get_from_db('address'))['confirmed']/result


    def get_from_db(self, pos):
        db = sqlite3.connect(__db_path__)
        cur = db.cursor()
        cur.execute(f'select {pos} from keys')
        r = cur.fetchone()[0]
        return r

    def dop(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    # Отправка транзакции
    def send_transaction(self):
        try:
            priv = self.get_from_db('private_key')
            address = self.get_from_db('address')
            inputs = self.btc.unspent(address)
            summ = int(float(self.ui.summ.text())*10** 8)
            outs = [{'value': summ, 'address': self.ui.addr.text()}, {'value': sum(i['value'] for i in inputs) - 10000 - 750 , 'address': address}]
            tx = self.btc.mktx(inputs, outs)
            tx2 = self.btc.signall(tx, priv)
            tx3 = serialize(tx2)
            self.ui.label.setText(self.btc.pushtx(tx3))
        except:
            QMessageBox.critical(self, 'Ошибка!', "Проверьте корректность введенных данных")





class FirstRunWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = firstrun_form.Ui_MainWindow()
        self.btc = Bitcoin(testnet=True)
        self.ui.setupUi(self)
        self.ui.create_wallet.clicked.connect(self.create_wallet)
        self.ui.import_wallet.clicked.connect(self.import_wallet)

    def import_wallet(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.check.clicked.connect(self.check_keys)
    def check_keys(self):
        try:
            private_key = self.ui.private_key_2.text()
            self.ui.public_key_2.setText(self.btc.privtopub(private_key))
            self.ui.address_2.setText(self.btc.pubtoaddr(self.btc.privtopub(private_key)))
            self.ui.finish_import.clicked.connect(self.add_keys_to_db(private_key, self.btc.pubtoaddr(self.btc.privtopub(private_key))))
        except:
            QMessageBox.critical(self, 'Ошибка!', "Проверьте корректность секретного ключа")





    def create_wallet(self):
        self.ui.stackedWidget.setCurrentIndex(2) # переход на сл страницу - создание кошелька
        self.ui.generate.clicked.connect(self.generate_keys)
        self.ui.go.setEnabled(True)

    def generate_keys(self):
        private_key = random_key()
        public_key = self.btc.privtopub(private_key)
        addr = self.btc.pubtoaddr(public_key)
        self.ui.private_key.setText("*"*40)
        self.ui.show_private_key.setEnabled(True)
        self.ui.public_key.setText(public_key)
        self.ui.address.setText(addr)
        self.ui.show_private_key.clicked.connect(lambda: self.ui.private_key.setText(private_key))
        self.ui.go.clicked.connect(self.add_keys_to_db(private_key, addr))

    # Функция добавления ключей в БД
    def add_keys_to_db(self, private_key, addr):
        db = sqlite3.connect('./wallet.db')
        cur = db.cursor()
        cur.execute('INSERT INTO keys (private_key, address) VALUES (?, ?)',(str(private_key), str(addr)))
        db.commit()
        db.close()





def init_db():
    db = sqlite3.connect('./wallet.db')
    cur = db.cursor()
    cur.execute("create table if not exists keys (private_key TEXT, address TEXT)")
    db.commit()
    cur.execute('select * from keys')
    if cur.fetchone() is not None: # если ключи есть - вернуть 1
        return 1
    db.close()

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
    def show_w1(self):
        self.w1 = FirstRunWindow()
        self.w1.ui.go.clicked.connect(self.show_w2)
        self.w1.ui.go.clicked.connect(self.w1.close)


        self.w1.ui.finish_import.clicked.connect(self.show_w2)
        self.w1.ui.finish_import.clicked.connect(self.w1.close)

        self.w1.show()

    def show_w2(self):
        self.w2 = MainWindow()
        self.w2.show()



if __name__ == "__main__":

    app = QApplication(sys.argv)
    widget = Main()
    Main().hide()
    widget.show()
    if init_db() == 1: # при наличии ключей запускается сразу MainWindow
        widget.show_w2()
    else:
        widget.show_w1() # при отсутствии ключей запускается мастер первоначальной настройки


    sys.exit(app.exec())
