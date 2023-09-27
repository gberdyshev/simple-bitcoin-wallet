# This Python file uses the following encoding: utf-8
import sys
import ui_form # Импорт основной формы
import ui_firstrun_form as firstrun_form
import sqlite3
import os
import time
import requests, json
from cryptos import *
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget, QDialog
__db_path__ = './db/wallet.db'
__data_db_path__ = './db/data.db'
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
        #self.ui.hello.setText(f'Здравствуйте, {self.get_from_db("address")}')
        self.ui.show_bal.clicked.connect(lambda: self.ui.balance.setText(str(self.get_bal('confirmed'))))
        self.ui.show_bal.clicked.connect(lambda: self.ui.unconf_balance.setText(str('{0:.9f}'.format(self.get_bal('unconfirmed')))))
        self.ui.receive_button.clicked.connect(self.recieve)


    def recieve(self): # !!!надо qr-код сделать!!!
        self.ui.stackedWidget.setCurrentIndex(1) # открытие страницы
        address = self.get_from_db('address')
        self.ui.address_label.setText(address)
        self.ui.address_label.clicked.connect(lambda: QApplication.clipboard().setText(address))




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
        result = pow(10, 8//2) # Оптимизация возведения 10^8
        result = result * result
        if 8 % 2 != 0:
            result = result * val
        return self.btc.get_balance(self.get_from_db('address'))[status]/result


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
        #try:
            priv = self.get_from_db('private_key')
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
            tx2 = self.btc.signall(tx, priv)
            tx3 = serialize(tx2)
            tx_final = self.btc.pushtx(tx3)
            linkTemplate = '<a href={0}>{1}</a>'
            tx_link = f'https://live.blockcypher.com/btc-testnet/tx/{tx_final}'
            self.ui.hash.setText(linkTemplate.format(tx_link, tx_final))

        #except:
            #QMessageBox.critical(self, 'Ошибка!', "Проверьте корректность введенных данных")





class FirstRunWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = firstrun_form.Ui_MainWindow()
        self.btc = Bitcoin(testnet=True)
        self.ui.setupUi(self)
        self.ui.create_wallet.clicked.connect(self.create_wallet)
        self.ui.import_wallet.clicked.connect(self.import_wallet)

    # !!!
    def add_old_transactions_to_db(self, address):
        history = self.btc.get_histories(address)
        db = sqlite3.connect(__db_path__)
        cur = db.cursor()
        for i in range(len(history)):
            tx_hash = history[i]['tx_hash']
            data = self.btc.inspect(self.btc.get_raw_tx(tx_hash))
            # если у нас есть адрес в ins, то транзакция типа "перевод OUT", если другой адрес "получение IN"
            if next(iter(data['ins'])) == address:
                for x in range(len(data['outs'])):
                    if data['outs'][x]['address'] == address:
                        continue
                    else:
                        print(data['outs'][x]['address'], data['outs'][x]['value'])
            else:
                print('')

            #r = requests.get(f'https://api.blockcypher.com/v1/btc/test3/txs/{tx_hash}?includeHex=false').json()






    def import_wallet(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.check.clicked.connect(self.check_keys)
    def check_keys(self):
        #try:


            private_key = self.ui.private_key_2.text()
            self.ui.public_key_2.setText(self.btc.privtopub(private_key))
            self.ui.address_2.setText(self.btc.pubtoaddr(self.btc.privtopub(private_key)))
            self.ui.finish_import.clicked.connect(lambda: self.add_keys_to_db(private_key, self.btc.pubtoaddr(self.btc.privtopub(private_key))))

            #self.ui.finish_import.clicked.connect(self.add_old_transactions_to_db(self.btc.pubtoaddr(self.btc.privtopub(private_key))))
        #except:
            #QMessageBox.critical(self, 'Ошибка!', "Проверьте корректность секретного ключа")


    def create_wallet(self):
        self.ui.stackedWidget.setCurrentIndex(2) # переход на сл страницу - создание кошелька
        self.ui.generate.clicked.connect(lambda: self.gen_keys())
        self.ui.go.setEnabled(True)

        self.ui.go.clicked.connect(lambda: self.add_keys_to_db(self.ui.private_key.text() ,  self.ui.address.text()))



    def generate_keys(self, private_key, public_key, addr):
        self.ui.private_key.setText(private_key)
        #self.ui.show_private_key.setEnabled(True)
        self.ui.public_key.setText(public_key)
        self.ui.address.setText(addr)
        #self.ui.show_private_key.clicked.connect(lambda: self.ui.private_key.setText(private_key))

        #self.ui.go.clicked.connect(lambda: self.add_keys_to_db(private_key, addr))

    def gen_keys(self):
        private_key = random_key()
        public_key = self.btc.privtopub(private_key)
        addr = self.btc.pubtoaddr(public_key)
        return self.generate_keys(private_key, public_key, addr)




    # Функция добавления ключей в БД
    def add_keys_to_db(self, private_key, addr):
        db = sqlite3.connect(__db_path__)
        cur = db.cursor()
        cur.execute('INSERT INTO keys (private_key, address) VALUES (?, ?)',(str(private_key), str(addr)))
        db.commit()
        db.close()





def init_db():
    db = sqlite3.connect(__db_path__)
    cur = db.cursor()
    cur.execute("create table if not exists keys (private_key TEXT, address TEXT)")
    cur.execute("create table if not exists transactions (address TEXT, type TEXT, hash TEXT, amount_sat INTEGER, recepient TEXT, fee INTEGER)")
    db.commit()
    cur.execute('select * from keys')
    if cur.fetchone() is not None: # если ключи есть - вернуть 1
        return 1
    return 0
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
