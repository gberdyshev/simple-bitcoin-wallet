# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QStackedWidget, QTabWidget, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1026, 533)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(220, 0, 831, 531))
        self.stackedWidget.setLineWidth(3)
        self.stackedWidget.setMidLineWidth(3)
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.label_3 = QLabel(self.home)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 10, 311, 31))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_3.setFont(font)
        self.stackedWidget.addWidget(self.home)
        self.receive_page = QWidget()
        self.receive_page.setObjectName(u"receive_page")
        self.tabWidget = QTabWidget(self.receive_page)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 791, 521))
        self.address_settings = QWidget()
        self.address_settings.setObjectName(u"address_settings")
        self.generate_new_addr = QPushButton(self.address_settings)
        self.generate_new_addr.setObjectName(u"generate_new_addr")
        self.generate_new_addr.setGeometry(QRect(270, 350, 231, 51))
        self.address_qr = QLabel(self.address_settings)
        self.address_qr.setObjectName(u"address_qr")
        self.address_qr.setGeometry(QRect(300, 40, 200, 200))
        self.address_qr.setMinimumSize(QSize(200, 200))
        self.address_qr.setMaximumSize(QSize(200, 200))
        self.address_qr.setSizeIncrement(QSize(0, 0))
        self.address_qr.setBaseSize(QSize(0, 0))
        self.address_label = QPushButton(self.address_settings)
        self.address_label.setObjectName(u"address_label")
        self.address_label.setGeometry(QRect(230, 280, 331, 26))
        self.address_label.setFlat(True)
        self.tabWidget.addTab(self.address_settings, "")
        self.address_viewer = QWidget()
        self.address_viewer.setObjectName(u"address_viewer")
        self.addresses_table = QTableWidget(self.address_viewer)
        self.addresses_table.setObjectName(u"addresses_table")
        self.addresses_table.setGeometry(QRect(10, 50, 771, 431))
        self.pushButton_2 = QPushButton(self.address_viewer)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 20, 141, 26))
        self.tabWidget.addTab(self.address_viewer, "")
        self.stackedWidget.addWidget(self.receive_page)
        self.send = QWidget()
        self.send.setObjectName(u"send")
        self.addr = QLineEdit(self.send)
        self.addr.setObjectName(u"addr")
        self.addr.setGeometry(QRect(80, 20, 311, 26))
        self.summ = QLineEdit(self.send)
        self.summ.setObjectName(u"summ")
        self.summ.setGeometry(QRect(80, 70, 311, 26))
        self.pushButton = QPushButton(self.send)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QRect(80, 210, 191, 71))
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoDefault(False)
        self.note = QLineEdit(self.send)
        self.note.setObjectName(u"note")
        self.note.setGeometry(QRect(80, 120, 311, 26))
        self.stackedWidget.addWidget(self.send)
        self.history_page = QWidget()
        self.history_page.setObjectName(u"history_page")
        self.history_table = QTableWidget(self.history_page)
        self.history_table.setObjectName(u"history_table")
        self.history_table.setEnabled(True)
        self.history_table.setGeometry(QRect(10, 80, 781, 441))
        self.history_table.setMidLineWidth(0)
        self.history_table.setSortingEnabled(False)
        self.history_table.setRowCount(0)
        self.debet = QLabel(self.history_page)
        self.debet.setObjectName(u"debet")
        self.debet.setGeometry(QRect(30, 20, 351, 18))
        self.credit = QLabel(self.history_page)
        self.credit.setObjectName(u"credit")
        self.credit.setGeometry(QRect(30, 50, 451, 18))
        self.filter_history = QComboBox(self.history_page)
        self.filter_history.setObjectName(u"filter_history")
        self.filter_history.setGeometry(QRect(590, 50, 201, 21))
        self.filter_history.setEditable(False)
        self.load_button = QPushButton(self.history_page)
        self.load_button.setObjectName(u"load_button")
        self.load_button.setGeometry(QRect(590, 10, 151, 31))
        self.stackedWidget.addWidget(self.history_page)
        self.lock = QWidget()
        self.lock.setObjectName(u"lock")
        self.password = QLineEdit(self.lock)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(210, 280, 301, 26))
        self.password_ok = QPushButton(self.lock)
        self.password_ok.setObjectName(u"password_ok")
        self.password_ok.setGeometry(QRect(280, 330, 151, 26))
        self.stackedWidget.addWidget(self.lock)
        self.send_confirm = QWidget()
        self.send_confirm.setObjectName(u"send_confirm")
        self.check_details = QLabel(self.send_confirm)
        self.check_details.setObjectName(u"check_details")
        self.check_details.setGeometry(QRect(40, 20, 221, 18))
        self.label_5 = QLabel(self.send_confirm)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 70, 141, 18))
        self.label_6 = QLabel(self.send_confirm)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 100, 141, 18))
        self.address_recipient = QLabel(self.send_confirm)
        self.address_recipient.setObjectName(u"address_recipient")
        self.address_recipient.setGeometry(QRect(180, 70, 601, 18))
        self.summ_recipient = QLabel(self.send_confirm)
        self.summ_recipient.setObjectName(u"summ_recipient")
        self.summ_recipient.setGeometry(QRect(180, 100, 141, 18))
        self.fee_options = QComboBox(self.send_confirm)
        self.fee_options.addItem("")
        self.fee_options.addItem("")
        self.fee_options.addItem("")
        self.fee_options.addItem("")
        self.fee_options.setObjectName(u"fee_options")
        self.fee_options.setGeometry(QRect(200, 170, 301, 31))
        self.fee_options.setEditable(False)
        self.check_details_2 = QLabel(self.send_confirm)
        self.check_details_2.setObjectName(u"check_details_2")
        self.check_details_2.setGeometry(QRect(230, 140, 261, 20))
        self.comm = QLabel(self.send_confirm)
        self.comm.setObjectName(u"comm")
        self.comm.setGeometry(QRect(200, 210, 141, 18))
        self.comission_byte = QLabel(self.send_confirm)
        self.comission_byte.setObjectName(u"comission_byte")
        self.comission_byte.setGeometry(QRect(360, 210, 141, 18))
        self.comm_2 = QLabel(self.send_confirm)
        self.comm_2.setObjectName(u"comm_2")
        self.comm_2.setGeometry(QRect(200, 240, 191, 51))
        self.comission_tr = QLabel(self.send_confirm)
        self.comission_tr.setObjectName(u"comission_tr")
        self.comission_tr.setGeometry(QRect(390, 260, 141, 18))
        self.push_transaction = QPushButton(self.send_confirm)
        self.push_transaction.setObjectName(u"push_transaction")
        self.push_transaction.setGeometry(QRect(240, 360, 211, 41))
        self.cancel_transaction = QPushButton(self.send_confirm)
        self.cancel_transaction.setObjectName(u"cancel_transaction")
        self.cancel_transaction.setGeometry(QRect(240, 440, 211, 41))
        self.password_2 = QLineEdit(self.send_confirm)
        self.password_2.setObjectName(u"password_2")
        self.password_2.setGeometry(QRect(200, 320, 301, 26))
        self.password_2.setClearButtonEnabled(True)
        self.stackedWidget.addWidget(self.send_confirm)
        self.send_success = QWidget()
        self.send_success.setObjectName(u"send_success")
        self.hash = QLabel(self.send_success)
        self.hash.setObjectName(u"hash")
        self.hash.setGeometry(QRect(30, 200, 761, 20))
        self.hash.setOpenExternalLinks(True)
        self.label_4 = QLabel(self.send_success)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(140, 150, 531, 18))
        self.stackedWidget.addWidget(self.send_success)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 20, 66, 18))
        self.balance = QLabel(self.centralwidget)
        self.balance.setObjectName(u"balance")
        self.balance.setGeometry(QRect(20, 60, 131, 18))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 90, 121, 18))
        self.label.setMouseTracking(False)
        self.unconf_balance = QLabel(self.centralwidget)
        self.unconf_balance.setObjectName(u"unconf_balance")
        self.unconf_balance.setGeometry(QRect(20, 120, 131, 18))
        self.menu_buttons = QGroupBox(self.centralwidget)
        self.menu_buttons.setObjectName(u"menu_buttons")
        self.menu_buttons.setEnabled(False)
        self.menu_buttons.setGeometry(QRect(0, 140, 221, 401))
        self.menu_buttons.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.menu_buttons.setAutoFillBackground(False)
        self.show_bal = QPushButton(self.menu_buttons)
        self.show_bal.setObjectName(u"show_bal")
        self.show_bal.setGeometry(QRect(20, 30, 181, 41))
        self.go_to_home = QPushButton(self.menu_buttons)
        self.go_to_home.setObjectName(u"go_to_home")
        self.go_to_home.setGeometry(QRect(20, 80, 181, 41))
        font1 = QFont()
        font1.setBold(True)
        self.go_to_home.setFont(font1)
        self.pushButton_3 = QPushButton(self.menu_buttons)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(20, 130, 181, 41))
        self.receive_button = QPushButton(self.menu_buttons)
        self.receive_button.setObjectName(u"receive_button")
        self.receive_button.setGeometry(QRect(20, 180, 181, 41))
        self.contacts = QPushButton(self.menu_buttons)
        self.contacts.setObjectName(u"contacts")
        self.contacts.setGeometry(QRect(20, 280, 181, 41))
        self.setting = QPushButton(self.menu_buttons)
        self.setting.setObjectName(u"setting")
        self.setting.setGeometry(QRect(20, 330, 181, 41))
        self.history = QPushButton(self.menu_buttons)
        self.history.setObjectName(u"history")
        self.history.setGeometry(QRect(20, 230, 181, 41))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(4)
        self.tabWidget.setCurrentIndex(0)
        self.filter_history.setCurrentIndex(-1)
        self.password_ok.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Simple Bitcoin (Testnet) Wallet", None))
        self.generate_new_addr.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043d\u043e\u0432\u044b\u0439 \u0430\u0434\u0440\u0435\u0441", None))
        self.address_qr.setText("")
        self.address_label.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.address_settings), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.address_viewer), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.addr.setText(QCoreApplication.translate("MainWindow", u"\u0430\u0434\u0440\u0435\u0441", None))
        self.summ.setText(QCoreApplication.translate("MainWindow", u"\u0441\u0443\u043c\u043c\u0430", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043b\u0435\u0435", None))
        self.note.setText(QCoreApplication.translate("MainWindow", u"\u043f\u0440\u0438\u043c\u0435\u0447\u0430\u043d\u0438\u0435 (\u0432\u0438\u0434\u043d\u043e \u0442\u043e\u043b\u044c\u043a\u043e \u0432\u0430\u043c)", None))
        self.debet.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435\u0433\u043e \u043f\u043e\u0441\u0442\u0443\u043f\u0438\u043b\u043e (\u0434\u0435\u0431\u0435\u0442):", None))
        self.credit.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435\u0433\u043e \u043e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u043e (\u043a\u0440\u0435\u0434\u0438\u0442, \u0431\u0435\u0437 \u0443\u0447\u0451\u0442\u0430 \u043a\u043e\u043c\u0438\u0441\u0441\u0438\u0438):", None))
        self.filter_history.setCurrentText("")
        self.load_button.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.password.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.password_ok.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0445\u043e\u0434", None))
        self.check_details.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u044c\u0442\u0435 \u0434\u0435\u0442\u0430\u043b\u0438 \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u0438", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0440\u0435\u0441 \u043f\u043e\u043b\u0443\u0447\u0430\u0442\u0435\u043b\u044f:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0443\u043c\u043c\u0430 \u043a \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0435:", None))
        self.address_recipient.setText("")
        self.summ_recipient.setText("")
        self.fee_options.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440", None))
        self.fee_options.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0411\u044b\u0441\u0442\u0440\u0430\u044f", None))
        self.fee_options.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u043d\u0434\u0430\u0440\u0442\u043d\u0430\u044f", None))
        self.fee_options.setItemText(3, QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0434\u043b\u0435\u043d\u043d\u0430\u044f", None))

        self.check_details_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f:", None))
        self.comm.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043c\u0438\u0441\u0441\u0438\u044f (sat/vB):", None))
        self.comission_byte.setText("")
        self.comm_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043c\u0438\u0441\u0441\u0438\u044f \u0437\u0430 \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u044e:", None))
        self.comission_tr.setText("")
        self.push_transaction.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0441\u0442\u0438", None))
        self.cancel_transaction.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u044e", None))
        self.password_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.hash.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u043f\u0435\u0448\u043d\u043e! \u0422\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u044f \u043f\u043e\u0434\u043f\u0438\u0441\u0430\u043d\u0430 \u0438 \u043f\u0435\u0440\u0435\u0434\u0430\u043d\u0430 \u0432 \u0441\u0435\u0442\u044c. \u041e\u0436\u0438\u0434\u0430\u0439\u0442\u0435 \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f.", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0410\u041b\u0410\u041d\u0421", None))
        self.balance.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u043e", None))
        self.unconf_balance.setText("")
        self.menu_buttons.setTitle("")
        self.show_bal.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0431\u0430\u043b\u0430\u043d\u0441", None))
        self.go_to_home.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043c\u043e\u0439", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        self.receive_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c", None))
        self.contacts.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u044b", None))
        self.setting.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.history.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u0442\u043e\u0440\u0438\u044f", None))
    # retranslateUi

