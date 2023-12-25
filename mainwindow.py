# This Python file uses the following encoding: utf-8
import sys
import sqlcipher3
import requests
import qrcode
import os
import threading
import time

from ui import ui_form # Импорт основной формы
from ui import ui_firstrun_form as firstrun_form


from scripts.database import Database
from scripts import consts

from cryptos import *
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget, QDialog, QTableWidgetItem, QInputDialog, QLineEdit
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QThread

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
    def __init__(self, parent=None):
        self.btc = __coin__
        super().__init__(parent)
        self.ui = ui_form.Ui_MainWindow()
        self.ui.setupUi(self)
        password, ok = QInputDialog.getText(None, 'Аутентификация', 'Введите пароль:', QLineEdit.Password)
        if Database(password).check_password() is False:
            quit()
        self.password = password
        self.ui.pushButton.clicked.connect(self.send_transaction)
        self.ui.pushButton_3.clicked.connect(self.dop)
        #self.ui.hello.setText(f'Здравствуйте, {self.get_from_db("address")}')

        self.ui.show_bal.clicked.connect(lambda: threading.Thread(target=self.get_bal).start())
        #self.ui.show_bal.clicked.connect(lambda: self.ui.unconf_balance.setText(str('{0:.9f}'.format(self.get_bal('unconfirmed')))))
        self.ui.receive_button.clicked.connect(self.recieve)
        self.ui.history.clicked.connect(self.get_history)
        self.ui.load_button.clicked.connect(self.update_history)
        self.ui.generate_new_addr.clicked.connect(lambda: self.generate_new_address())
        self.ui.go_to_home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.pushButton_2.clicked.connect(self.get_addresses)

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
        db1 = sqlcipher3.connect(__db_path__)
        cur1 = db1.cursor()
        cur1.execute('select * from keys')
        r = cur1.fetchall()
        self.ui.addresses_table.setRowCount(len(r)) # строчки
        self.ui.addresses_table.setColumnCount(1)
        self.ui.addresses_table.setHorizontalHeaderLabels(["Адрес"])
        print(r)
        for i, (public_key, address) in enumerate(r):
            self.ui.addresses_table.setItem(i,0, QTableWidgetItem(address))


    def generate_new_address(self):
        db = sqlcipher3.connect(__wallet_db_path__)
        cur = db.cursor()
        cur.execute('PRAGMA KEY = "{}"'.format(self.password))
        cur.execute("select mnemonic from mnemonic_keys")
        r = cur.fetchone()
        #print(r)
        wallet = self.btc.wallet(r[0])
        #print(wallet.get_used_addresses())

        db1 = sqlcipher3.connect(__db_path__)
        cur1 = db1.cursor()
        cur1.execute('select address from keys')
        r = cur1.fetchall()
        print(r)
        new_address_index = len(r)

        new_addr = wallet.receiving_address(new_address_index)
        priv_key = wallet.privkey(new_addr)
        public_key = self.btc.privtopub(wallet.privkey(new_addr))
        cur1.execute('INSERT INTO keys (public_key, address) VALUES (?, ?)',(public_key, new_addr))
        db1.commit()
        cur.execute('INSERT INTO keys (private_key, public_key, address) VALUES (?, ?, ?)',(priv_key, public_key, new_addr))
        db.commit()

        self.ui.address_label.setText(new_addr)
        return new_addr







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


    def get_bal(self):
        db1 = sqlcipher3.connect(__db_path__)
        cur1 = db1.cursor()
        cur1.execute('select address from keys')
        r = cur1.fetchall()
        confirmed_bal = 0
        unconfirmed_bal = 0
        addresses = []
        for addr in r:
            addresses.append(addr[0])
            #dict_bal = self.btc.get_balance(addr[0])
            #confirmed_bal += dict_bal['confirmed']
            #unconfirmed_bal += dict_bal['unconfirmed']
            #print(addr, dict_bal['confirmed'])
        bal = self.btc.get_balances(*tuple(addresses))
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

    # Отправка транзакции
    def send_transaction(self):
        #try:
            #priv = self.get_from_db('private_key')
            #address = self.get_from_db('address')
            t = time.time()
            summ = round(float(self.ui.summ.text())*10**8)
            db = sqlcipher3.connect(__wallet_db_path__)
            cur = db.cursor()
            cur.execute('PRAGMA KEY = "{}"'.format(self.password))
            cur.execute("select address, private_key from keys")
            r = cur.fetchall()
            #db1 = sqlcipher3.connect(__db_path__)
            #cur1 = db1.cursor()
            #cur1.execute('select address from keys')
            #r = cur1.fetchall()
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

            fee = (len(inputs) * 148 + 2 * 34 + 10) * 1 # 2 - это выходы, пока они захардажены
            print(inputs, priv)
            print(inputs_summ)
            print(time.time()-t)

            last_address = Database(self.password).get_last_address()
            if len(self.btc.unspent(last_address)) == 0:
                new_addr = last_address
            else:
                new_addr = self.generate_new_address()
            #Сдача считается по формуле: входные данные - сумма отправки - комиссия
            if inputs_summ - summ - fee < 0 or summ <=0:
                return QMessageBox.critical(self, 'Ошибка!', "Недостаточно средств на счёте")
            elif self.btc.is_address(self.ui.addr.text()) is False:
                return QMessageBox.critical(self, 'Ошибка!', "Неверный адрес получателя")
            outs = [{'value': summ, 'address': self.ui.addr.text()}, {'value': inputs_summ -  summ - fee, 'address': new_addr}]
            tx = self.btc.mktx(inputs, outs)
            password, ok = QInputDialog.getText(None, 'Подписание транзакции', 'Введите пароль:', QLineEdit.Password)
            check_password = Database(str(password)).check_password()
            if check_password is not False:
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
        db = sqlcipher3.connect(__db_path__)
        cur = db.cursor()
        cur.execute("delete from transactions")
        db.commit()
        self.ui.finish_import_2.clicked.connect(lambda: self.add_password(self.ui.private_key_2.text(),self.ui.public_key_2.text(), self.ui.address_2.text()))

        # !!!
    def add_old_transactions_to_db(self):
        addr_list = Database().get_addresses_from_db()
        history = self.btc.get_histories(*tuple(addr_list))
        db = sqlcipher3.connect(__db_path__)
        value = self.ui.import_progress.value()
        cur = db.cursor()
        print(history)
        for i in range(len(history)):
            tx_hash = history[i]['tx_hash']
            r = cur.execute('select * from transactions where hash = ?', (tx_hash,))
            if r.fetchone() is None and history[i]['height'] > 0:
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
                            cur.execute('INSERT INTO transactions (type, sender, recepient, hash, amount, fee) VALUES (?, ?, ?, ?, ?, ?)', (type, sender, recepient, tx_hash, amount, fee))
                            #db.commit()
                    else:
                        if data['outs'][x]['address'] in addr_list:
                            type = 'input'
                            sender = next(iter(data['ins']))
                            recepient = 'You'
                            amount = data['outs'][x]['value']
                            fee = data['fee']
                            cur.execute('INSERT INTO transactions (type, sender, recepient, hash, amount, fee) VALUES (?, ?, ?, ?, ?, ?)', (type, sender, recepient, tx_hash, amount, fee))
                    db.commit()
                    self.ui.import_progress.setValue(value+int(100/len(history)))
                    value += int(100/len(history))
        self.ui.import_progress.setValue(100)
        print("б")
        self.ui.finish_import_2.setEnabled(True)
        #self.w2 = MainWindow()
        #self.ui.finish_import.clicked.connect(self.close())
        #self.ui.finish_import.clicked.connect(self.w2.show())



    def check_keys(self):
        try:
            private_key = self.ui.private_key_2.text()
            public_key = self.btc.privtopub(private_key)
            self.ui.public_key_2.setText(public_key)
            self.ui.address_2.setText(self.btc.pubtoaddr(self.btc.privtopub(private_key)))
            #self.ui.finish_import.clicked.connect(lambda: self.add_keys_to_db(public_key, self.btc.pubtoaddr(public_key)))
            self.ui.finish_import.clicked.connect(lambda: self.add_old_transactions_to_db(self.btc.pubtoaddr(public_key)))
        except:
            QMessageBox.critical(self, 'Ошибка!', "Проверьте корректность секретного ключа")

    def crypt_wdb(self, private_key, public_key, address, mnemonic):

        wdb = sqlcipher3.connect(__wallet_db_path__)
        cur = wdb.cursor()
        cur.execute('PRAGMA KEY = "{}"'.format(self.ui.password.text()))
        wdb.commit()
        cur.execute("create table if not exists keys (private_key TEXT, public_key TEXT, address TEXT)")
        cur.execute("create table if not exists mnemonic_keys (mnemonic TEXT)")
        cur.execute('INSERT INTO keys (private_key, public_key, address) VALUES (?, ?, ?)',(private_key, public_key, address))
        cur.execute('INSERT INTO mnemonic_keys (mnemonic) VALUES (?)',(mnemonic,))
        wdb.commit()
        self.add_keys_to_db(public_key, address)


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




    # Функция добавления ключей в БД
    def add_keys_to_db(self, public_key, addr):
        db = sqlcipher3.connect(__db_path__)
        cur = db.cursor()
        r = cur.execute('select * from keys where public_key = ?',(public_key,))
        if r.fetchone() is None:
            cur.execute('INSERT INTO keys (public_key, address) VALUES (?, ?)',(str(public_key), str(addr)))
        #cur.execute('INSERT INTO mnemonic_public_key (xpub_key) VALUES (?)',(xpub_key))
        db.commit()





def init():
    if not os.path.exists(__temp_path__):
        os.mkdir(__temp_path__)
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
    if cur.fetchone() is not None and os.path.exists(__wallet_db_path__): # если ключи есть и есть файл с БД кошелька - вернуть 1
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
