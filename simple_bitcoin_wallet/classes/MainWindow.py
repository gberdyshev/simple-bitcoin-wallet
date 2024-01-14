"""Основное окно приложения"""

import sqlcipher3
import threading
import time

from simple_bitcoin_wallet.ui import ui_form # Импорт основной формы

# Импорт самописных функций
from simple_bitcoin_wallet.scripts.wallets import GeneralFunctions
from simple_bitcoin_wallet.scripts.tools import Tools
from simple_bitcoin_wallet.scripts.database import Database
from simple_bitcoin_wallet.scripts import consts

from cryptos import *
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget, QDialog, QTableWidgetItem, QInputDialog, QLineEdit
from PySide6.QtGui import QImage, QPixmap, QFont

__db_folder_path__ = consts.__db_folder_path__
__db_path__ = consts.__db_path__
__wallet_db_path__ = consts.__wallet_db_path__ # Зашифрованная база для хранения секретного ключа
__temp_path__ = consts.__temp_path__
__coin__ = Bitcoin(testnet=consts.__testnet__) # Какую монету используем, какую сеть
__currency__ = consts.__currency__ # если 10^8 - Биткоин, если 1 - сатоши (10^(-8) Биткоина)


class MainWindow(QMainWindow):
    def __init__(self, parent=None, FirstRun=False, password=None):
        self.btc = __coin__
        super().__init__(parent)
        self.ui = ui_form.Ui_MainWindow()
        self.ui.setupUi(self)
        self.check_theme()
        self.ui.address_label.clicked.connect(lambda: QApplication.clipboard().setText(self.ui.address_label.text()))

        self.ui.addresses_list.itemActivated.connect(self.address_item_change)
        self.ui.change_theme.clicked.connect(self.change_theme)
        self.ui.history_table.currentItemChanged.connect(lambda: self.get_transaction_inform(self.ui.history_table.item(self.ui.history_table.currentRow(),1).text()))
        self.ui.password_ok.clicked.connect(self.enter_to_wallet)
        self.password = password
        self.ui.pushButton.clicked.connect(self.prepare_transaction)
        self.ui.push_transaction.clicked.connect(lambda: self.send_transaction(self.inputs, self.priv, self.inputs_summ, self.summ, self.new_addr))
        self.ui.pushButton_3.clicked.connect(self.dop)
        self.ui.contacts.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(7))

        self.ui.setting.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(9))
        self.ui.get_mnemonic.clicked.connect(self.get_mnemonic)
        self.ui.show_bal.clicked.connect(lambda: threading.Thread(target=self.get_bal).start())
        self.ui.receive_button.clicked.connect(self.recieve)
        self.ui.history.clicked.connect(self.get_history)

        self.ui.load_button.clicked.connect(lambda: threading.Thread(target=self.update_history).start())
        self.ui.generate_new_addr.clicked.connect(lambda: self.generate_new_address())
        self.ui.go_to_home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.pushButton_2.clicked.connect(self.get_addresses)

    # Вход в кошелек, проверка пароля
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
            path = 'simple_bitcoin_wallet/resources/logo.png'
            self.ui.logo.setPixmap(QPixmap(path))         
            self.ui.docs.setText(consts.__linkTemplate__.format(consts.__docs__, "Документация"))   
            self.ui.source_code.setText(consts.__linkTemplate__.format(consts.__repository__, "Исходный код"))
            self.ui.author.setText(consts.__linkTemplate__.format(consts.__author__, "Связь с автором"))
        else:
            QMessageBox.critical(self, 'Ошибка!', "Неверный пароль")

    # Баланс
    def get_bal(self):
        addresses = Database().get_addresses_from_db()
        bal = self.btc.get_balances(*tuple(addresses))
        confirmed_bal = unconfirmed_bal = 0
        for i in bal:
            confirmed_bal += i['confirmed']
            unconfirmed_bal += i['unconfirmed']
        self.ui.balance.setText('{:.8f}'.format(confirmed_bal/__currency__))
        self.ui.unconf_balance.setText('{:.8f}'.format(unconfirmed_bal/__currency__))

    """ Настройки """
    def get_mnemonic(self):
        if self.ui.mnemonic.text() == "":
            password, ok = QInputDialog.getText(None, 'Подтверждение действия', 'Введите пароль:', QLineEdit.Password)
            check_password = Database(str(password)).check_password()
            if check_password:
                #QMessageBox.warning(self, 'Предупреждение!', "Никогда и никому не передавайте сид-фразу и секретные ключи от вашего кошелька!")
                if self.cr_DB.walletIsDeterministic() is False:
                    text = self.cr_DB.get_private_key_for_non_determ()
                else:
                    text = self.cr_DB.get_mnemonic()
                self.ui.mnemonic.setText(text)
            else:
                QMessageBox.critical(self, 'Ошибка!', "Неверный пароль") 
        else:
            self.ui.mnemonic.setText("")

    """ Работа с темой """

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

    """ Работа с историей транзакций """

    def update_history(self):
        GeneralFunctions().add_transactions()
        self.get_history()

    # Заполнение таблицы с транзакциями из БД
    def get_history(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        db = sqlcipher3.connect(__db_path__)
        cur = db.cursor()
        cur.execute('select * from transactions')
        r = cur.fetchall()
        self.ui.history_table.setRowCount(len(r)) # строчки
        #self.ui.history_table.setShowGrid(False)
        #self.ui.history_table.setHorizontalHeaderLabels(["Тип", "Хеш", "Сумма"])
        for i, (type, sender, recipient, hash, amount, fee) in enumerate(r):
            self.ui.history_table.setItem(i,0, QTableWidgetItem(type))

            self.ui.history_table.setItem(i,1, QTableWidgetItem(hash))
            self.ui.history_table.setItem(i,2, QTableWidgetItem(str('{:.8f}'.format(amount/__currency__))))

    """ Работа с адресами, генерацией адресов, таблицами адресов """

    def get_addresses(self):
        r = self.DB.get_addresses_from_db() # получаем адреса из базы данных
        self.ui.addresses_list.clear()
        for i, address in enumerate(r):
            self.ui.addresses_list.addItem(address) # фомируем список

    def get_transaction_inform(self, hash):
        db = sqlcipher3.connect(__db_path__)
        cur = db.cursor()
        cur.execute("select * from transactions where hash = ?", (hash, ))
        r = cur.fetchone()
        if r[0] == 'input':
            self.ui.summ_2.setText("+ {:.8f}".format(r[4]/__currency__))
        else:
            self.ui.summ_2.setText("-{:.8f}".format(r[4]/__currency__))

        self.ui.hash_2.setText(r[3])
        data = self.btc.inspect(self.btc.get_raw_tx(hash))
        outputs = data['outs']
        inputs = data['ins']
        self.ui.fee.setText(str('{:.8f}'.format(data['fee']/__currency__)))
        self.ui.outs_table.setRowCount(len(outputs))
        self.ui.inputs_table.setRowCount(len(inputs))

        """ Отбор входных и выходных данных транзакции """
        for i, out in enumerate(outputs):
            self.ui.outs_table.setItem(i,0, QTableWidgetItem(out['address']))
            self.ui.outs_table.setItem(i,1, QTableWidgetItem(str('{:.8f}'.format(out['value']/__currency__))))

        for i, input in enumerate(inputs):
            self.ui.inputs_table.setItem(i, 0, QTableWidgetItem(input))
            self.ui.inputs_table.setItem(i, 1, QTableWidgetItem(str('{:.8f}'.format(inputs[input]/__currency__))))
        self.ui.stackedWidget.setCurrentIndex(8)

    def generate_new_address(self):
        # если кошелек недетерминированный - генерация новых адресов невозможна
        if Database(self.password).walletIsDeterministic() is False: 
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

    def address_item_change(self, item):
        QApplication.clipboard().setText(item.text())


    """ Работа с транзакциями """

    def dop(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    # Подтверждение и отправка транзакций
    def send_transaction(self, inputs, priv, inputs_summ, summ, new_addr):
        if inputs_summ - summ - int(self.ui.comission_tr.text()) < 0:
            return QMessageBox.critical(self, 'Ошибка!', "Недостаточно средств на счёте")
        summ = int(float(self.ui.summ_recipient.text())*__currency__)
        outs = [{'value': summ, 'address': self.ui.address_recipient.text()},\
                {'value': inputs_summ -  summ - int(self.ui.comission_tr.text()), 'address': new_addr}]
        tx = self.btc.mktx(inputs, outs)
        password, ok = QInputDialog.getText(None, 'Подписание транзакции', 'Введите пароль:', QLineEdit.Password)
        check_password = Database(str(password)).check_password()
        if check_password:
            tx2 = self.btc.signall(tx, priv)
            tx3 = serialize(tx2)
            tx_final = self.btc.pushtx(tx3)
            tx_link = f'https://mempool.space/testnet/tx/{tx_final}'
            self.ui.hash.setText(consts.__linkTemplate__.format(tx_link, tx_final)) # Ссылка на проводник блокчейна
            self.ui.stackedWidget.setCurrentIndex(6)
        else:
            QMessageBox.critical(self, 'Ошибка!', "Неверный пароль")

    # Подготовка транзакции
    def prepare_transaction(self):
        try:
            t = time.time()
            summ = round(float(self.ui.summ.text())*__currency__)
            db = sqlcipher3.connect(__wallet_db_path__)
            cur = db.cursor()
            cur.execute('PRAGMA KEY = "{}"'.format(self.password))
            cur.execute("select address, private_key from keys")
            r = cur.fetchall()
            if self.btc.is_address(self.ui.addr.text()) is False:
                return QMessageBox.critical(self, 'Ошибка!', "Неверный адрес получателя")
            inputs_summ = 0
            all_in = []
            inputs = []
            priv = {}

            # Добавляем в список все сгенерированные адреса
            for addr in r:
                all_in.append(addr[0])
            all_in = tuple(all_in)
            all_in = self.btc.get_unspents(*all_in) # получаем UTXO для всех адресов

            # Добавляем неизрасходованные данные (UTXO)
            for unsp in all_in:
                if inputs_summ <= summ:
                    inputs.append(unsp)
                    addr = unsp['address']
                    priv[addr] = Database(self.password).get_private_key(addr)
                    inputs_summ += unsp['value']
       
            last_address = Database(self.password).get_last_address()

            # Если кошелек детерминированный - генерируем новый адрес для сдачи
            if len(self.btc.unspent(last_address)) == 0 or Database(self.password).walletIsDeterministic() is False:
                new_addr = last_address
            elif Database(self.password).walletIsDeterministic() is True:
                new_addr = self.GenFunc.generate_new_address()

            if inputs_summ - summ < 0 or summ <=0:
                return QMessageBox.critical(self, 'Ошибка!', "Недостаточно средств на счёте")

            # Получение сведений о комиссии
            def select_fee_option(value):
                fees = Tools().get_actual_fee()
                fee = 1
                if fees is False:
                    fee = 1
                    value = None
                if value == "Быстрая":
                    fee = fees[0]
                elif value == "Стандартная":
                    fee = fees[1]
                elif value == "Медленная":
                    fee = fees[2]
                
                fee_tr = Tools().calc_fee(len(inputs), 2, fee)
                self.ui.comission_byte.setText(str(fee))
                self.ui.comission_tr.setText(str(fee_tr))
            

            self.ui.stackedWidget.setCurrentIndex(5) # переход на страницу подтверждения транзакции
            self.ui.address_recipient.setText(self.ui.addr.text())
            self.ui.summ_recipient.setText(self.ui.summ.text())

            # Очистка всех полей после завершения транзакции
            self.ui.addr.setText("")
            self.ui.summ.setText("")
            self.ui.fee_options.setCurrentText("Выбор")
            self.ui.comission_byte.setText("")
            self.ui.comission_tr.setText("")
            self.ui.fee_options.currentTextChanged.connect(select_fee_option)
            self.inputs, self.priv, self.inputs_summ, self.summ, self.new_addr = inputs, priv, inputs_summ, summ, new_addr
            print(time.time()-t)
            self.ui.cancel_transaction.clicked.connect(self.dop)
        except:
            QMessageBox.critical(self, 'Ошибка!', "Проверьте корректность введенных данных")
