# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1026, 533)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(210, 0, 811, 531))
        self.stackedWidget.setLineWidth(3)
        self.stackedWidget.setMidLineWidth(3)
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.title = QLabel(self.home)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(290, 0, 151, 31))
        font = QFont()
        font.setFamilies([u"Cantarell"])
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.title.setFont(font)
        self.title.setAlignment(Qt.AlignCenter)
        self.logo = QLabel(self.home)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(310, 120, 108, 167))
        self.logo.setPixmap(QPixmap(u"../resources/logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.logo.setOpenExternalLinks(False)
        self.info = QFrame(self.home)
        self.info.setObjectName(u"info")
        self.info.setGeometry(QRect(110, 300, 511, 36))
        font1 = QFont()
        font1.setKerning(True)
        self.info.setFont(font1)
        self.info.setStyleSheet(u"a:hover, a:visited, a:link, a:active\n"
"{\n"
"    text-decoration: none;\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(self.info)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.author = QLabel(self.info)
        self.author.setObjectName(u"author")
        self.author.setAlignment(Qt.AlignCenter)
        self.author.setOpenExternalLinks(True)

        self.horizontalLayout.addWidget(self.author)

        self.docs = QLabel(self.info)
        self.docs.setObjectName(u"docs")
        self.docs.setStyleSheet(u"a:hover, a:visited, a:link, a:active\n"
"{\n"
"    text-decoration: none;\n"
"}")
        self.docs.setAlignment(Qt.AlignCenter)
        self.docs.setOpenExternalLinks(True)

        self.horizontalLayout.addWidget(self.docs)

        self.source_code = QLabel(self.info)
        self.source_code.setObjectName(u"source_code")
        self.source_code.setAlignment(Qt.AlignCenter)
        self.source_code.setOpenExternalLinks(True)

        self.horizontalLayout.addWidget(self.source_code)

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
        self.address_frame = QFrame(self.address_settings)
        self.address_frame.setObjectName(u"address_frame")
        self.address_frame.setGeometry(QRect(200, 40, 371, 291))
        self.address_qr = QLabel(self.address_frame)
        self.address_qr.setObjectName(u"address_qr")
        self.address_qr.setGeometry(QRect(90, 10, 200, 200))
        self.address_qr.setMinimumSize(QSize(200, 200))
        self.address_qr.setMaximumSize(QSize(200, 200))
        self.address_qr.setSizeIncrement(QSize(0, 0))
        self.address_qr.setBaseSize(QSize(0, 0))
        self.address_qr.setAlignment(Qt.AlignCenter)
        self.address_label = QPushButton(self.address_frame)
        self.address_label.setObjectName(u"address_label")
        self.address_label.setGeometry(QRect(3, 215, 371, 26))
        self.address_label.setFlat(True)
        self.label_3 = QLabel(self.address_settings)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(310, 10, 151, 18))
        self.label_3.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.address_settings, "")
        self.address_viewer = QWidget()
        self.address_viewer.setObjectName(u"address_viewer")
        self.pushButton_2 = QPushButton(self.address_viewer)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 20, 141, 26))
        self.addresses_list = QListWidget(self.address_viewer)
        self.addresses_list.setObjectName(u"addresses_list")
        self.addresses_list.setGeometry(QRect(5, 51, 771, 431))
        self.tabWidget.addTab(self.address_viewer, "")
        self.stackedWidget.addWidget(self.receive_page)
        self.send = QWidget()
        self.send.setObjectName(u"send")
        self.label_10 = QLabel(self.send)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(200, 40, 371, 21))
        self.label_10.setLayoutDirection(Qt.LeftToRight)
        self.label_10.setLineWidth(7)
        self.label_10.setTextFormat(Qt.PlainText)
        self.label_10.setScaledContents(False)
        self.label_10.setAlignment(Qt.AlignCenter)
        self.layoutWidget = QWidget(self.send)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(47, 100, 701, 251))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.transaction_frame = QFrame(self.layoutWidget)
        self.transaction_frame.setObjectName(u"transaction_frame")
        font2 = QFont()
        font2.setFamilies([u"Cantarell"])
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setKerning(True)
        self.transaction_frame.setFont(font2)
        self.transaction_frame.setStyleSheet(u"border: none;")
        self.verticalLayout_7 = QVBoxLayout(self.transaction_frame)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_5.setContentsMargins(0, 2, -1, -1)
        self.label_8 = QLabel(self.transaction_frame)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_5.addWidget(self.label_8)

        self.addr = QLineEdit(self.transaction_frame)
        self.addr.setObjectName(u"addr")
        self.addr.setStyleSheet(u"")
        self.addr.setClearButtonEnabled(True)

        self.verticalLayout_5.addWidget(self.addr)


        self.verticalLayout_7.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_9 = QLabel(self.transaction_frame)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_6.addWidget(self.label_9)

        self.summ = QLineEdit(self.transaction_frame)
        self.summ.setObjectName(u"summ")
        self.summ.setClearButtonEnabled(True)

        self.verticalLayout_6.addWidget(self.summ)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)


        self.gridLayout.addWidget(self.transaction_frame, 0, 0, 1, 1)

        self.trans_button = QVBoxLayout()
        self.trans_button.setObjectName(u"trans_button")
        self.line = QFrame(self.layoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.trans_button.addWidget(self.line)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        self.pushButton.setFont(font2)
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoDefault(False)

        self.trans_button.addWidget(self.pushButton)


        self.gridLayout.addLayout(self.trans_button, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.send)
        self.history_page = QWidget()
        self.history_page.setObjectName(u"history_page")
        self.history_table = QTableWidget(self.history_page)
        if (self.history_table.columnCount() < 3):
            self.history_table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.history_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.history_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.history_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.history_table.setObjectName(u"history_table")
        self.history_table.setEnabled(True)
        self.history_table.setGeometry(QRect(10, 80, 781, 441))
        self.history_table.setStyleSheet(u"border: none;")
        self.history_table.setMidLineWidth(0)
        self.history_table.setAutoScroll(True)
        self.history_table.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)
        self.history_table.setSortingEnabled(False)
        self.history_table.setRowCount(0)
        self.filter_history = QComboBox(self.history_page)
        self.filter_history.setObjectName(u"filter_history")
        self.filter_history.setGeometry(QRect(590, 50, 201, 21))
        self.filter_history.setEditable(False)
        self.load_button = QPushButton(self.history_page)
        self.load_button.setObjectName(u"load_button")
        self.load_button.setGeometry(QRect(590, 10, 151, 31))
        self.label_15 = QLabel(self.history_page)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(290, 10, 151, 18))
        self.stackedWidget.addWidget(self.history_page)
        self.lock = QWidget()
        self.lock.setObjectName(u"lock")
        self.password_frame = QFrame(self.lock)
        self.password_frame.setObjectName(u"password_frame")
        self.password_frame.setGeometry(QRect(200, 200, 401, 111))
        self.verticalLayout_13 = QVBoxLayout(self.password_frame)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.password = QLineEdit(self.password_frame)
        self.password.setObjectName(u"password")
        self.password.setStyleSheet(u"border: none;")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.password.setClearButtonEnabled(True)

        self.verticalLayout_13.addWidget(self.password)

        self.password_ok = QPushButton(self.password_frame)
        self.password_ok.setObjectName(u"password_ok")

        self.verticalLayout_13.addWidget(self.password_ok)

        self.stackedWidget.addWidget(self.lock)
        self.send_confirm = QWidget()
        self.send_confirm.setObjectName(u"send_confirm")
        self.verticalLayout_12 = QVBoxLayout(self.send_confirm)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.check_details = QLabel(self.send_confirm)
        self.check_details.setObjectName(u"check_details")
        self.check_details.setStyleSheet(u"font: 14pt \"Cantarell\";")

        self.verticalLayout_12.addWidget(self.check_details)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_5 = QLabel(self.send_confirm)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_8.addWidget(self.label_5)

        self.address_recipient = QLabel(self.send_confirm)
        self.address_recipient.setObjectName(u"address_recipient")

        self.verticalLayout_8.addWidget(self.address_recipient)


        self.verticalLayout_12.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_6 = QLabel(self.send_confirm)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_9.addWidget(self.label_6)

        self.summ_recipient = QLabel(self.send_confirm)
        self.summ_recipient.setObjectName(u"summ_recipient")

        self.verticalLayout_9.addWidget(self.summ_recipient)


        self.verticalLayout_12.addLayout(self.verticalLayout_9)

        self.check_details_2 = QLabel(self.send_confirm)
        self.check_details_2.setObjectName(u"check_details_2")
        self.check_details_2.setStyleSheet(u"font: 14pt \"Cantarell\";")

        self.verticalLayout_12.addWidget(self.check_details_2)

        self.fee_options = QComboBox(self.send_confirm)
        self.fee_options.addItem("")
        self.fee_options.addItem("")
        self.fee_options.addItem("")
        self.fee_options.addItem("")
        self.fee_options.setObjectName(u"fee_options")
        self.fee_options.setEditable(False)

        self.verticalLayout_12.addWidget(self.fee_options)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.comm = QLabel(self.send_confirm)
        self.comm.setObjectName(u"comm")

        self.verticalLayout_10.addWidget(self.comm)

        self.comission_byte = QLabel(self.send_confirm)
        self.comission_byte.setObjectName(u"comission_byte")

        self.verticalLayout_10.addWidget(self.comission_byte)


        self.verticalLayout_12.addLayout(self.verticalLayout_10)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.comm_2 = QLabel(self.send_confirm)
        self.comm_2.setObjectName(u"comm_2")

        self.verticalLayout_11.addWidget(self.comm_2)

        self.comission_tr = QLabel(self.send_confirm)
        self.comission_tr.setObjectName(u"comission_tr")

        self.verticalLayout_11.addWidget(self.comission_tr)


        self.verticalLayout_12.addLayout(self.verticalLayout_11)

        self.push_transaction = QPushButton(self.send_confirm)
        self.push_transaction.setObjectName(u"push_transaction")

        self.verticalLayout_12.addWidget(self.push_transaction)

        self.cancel_transaction = QPushButton(self.send_confirm)
        self.cancel_transaction.setObjectName(u"cancel_transaction")

        self.verticalLayout_12.addWidget(self.cancel_transaction)

        self.stackedWidget.addWidget(self.send_confirm)
        self.send_success = QWidget()
        self.send_success.setObjectName(u"send_success")
        self.hash = QLabel(self.send_success)
        self.hash.setObjectName(u"hash")
        self.hash.setGeometry(QRect(30, 200, 771, 20))
        self.hash.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.hash.setAlignment(Qt.AlignCenter)
        self.hash.setOpenExternalLinks(True)
        self.label_4 = QLabel(self.send_success)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(140, 150, 531, 18))
        self.label_4.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.send_success)
        self.contacts_2 = QWidget()
        self.contacts_2.setObjectName(u"contacts_2")
        self.label_11 = QLabel(self.contacts_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 30, 101, 18))
        self.stackedWidget.addWidget(self.contacts_2)
        self.transaction_inform = QWidget()
        self.transaction_inform.setObjectName(u"transaction_inform")
        self.transaction_inform.setStyleSheet(u"")
        self.hash_2 = QLabel(self.transaction_inform)
        self.hash_2.setObjectName(u"hash_2")
        self.hash_2.setGeometry(QRect(50, 180, 711, 18))
        self.hash_2.setAlignment(Qt.AlignCenter)
        self.summ_2 = QLabel(self.transaction_inform)
        self.summ_2.setObjectName(u"summ_2")
        self.summ_2.setGeometry(QRect(310, 130, 191, 41))
        font3 = QFont()
        font3.setFamilies([u"Cantarell"])
        font3.setPointSize(16)
        font3.setBold(False)
        font3.setItalic(False)
        self.summ_2.setFont(font3)
        self.summ_2.setStyleSheet(u"font: 16pt \"Cantarell\";")
        self.summ_2.setAlignment(Qt.AlignCenter)
        self.layoutWidget1 = QWidget(self.transaction_inform)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 250, 781, 261))
        self.in_outs = QHBoxLayout(self.layoutWidget1)
        self.in_outs.setObjectName(u"in_outs")
        self.in_outs.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_7 = QLabel(self.layoutWidget1)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_15.addWidget(self.label_7)

        self.inputs_table = QTableWidget(self.layoutWidget1)
        if (self.inputs_table.columnCount() < 2):
            self.inputs_table.setColumnCount(2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.inputs_table.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.inputs_table.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        self.inputs_table.setObjectName(u"inputs_table")

        self.verticalLayout_15.addWidget(self.inputs_table)


        self.in_outs.addLayout(self.verticalLayout_15)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_12 = QLabel(self.layoutWidget1)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_16.addWidget(self.label_12)

        self.outs_table = QTableWidget(self.layoutWidget1)
        if (self.outs_table.columnCount() < 2):
            self.outs_table.setColumnCount(2)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.outs_table.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.outs_table.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        self.outs_table.setObjectName(u"outs_table")

        self.verticalLayout_16.addWidget(self.outs_table)


        self.in_outs.addLayout(self.verticalLayout_16)

        self.layoutWidget2 = QWidget(self.transaction_inform)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(290, 210, 251, 21))
        self.fee_frame = QHBoxLayout(self.layoutWidget2)
        self.fee_frame.setObjectName(u"fee_frame")
        self.fee_frame.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.layoutWidget2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.fee_frame.addWidget(self.label_13)

        self.fee = QLabel(self.layoutWidget2)
        self.fee.setObjectName(u"fee")
        self.fee.setAlignment(Qt.AlignCenter)

        self.fee_frame.addWidget(self.fee)

        self.summ_3 = QLabel(self.transaction_inform)
        self.summ_3.setObjectName(u"summ_3")
        self.summ_3.setGeometry(QRect(310, 40, 191, 41))
        self.summ_3.setFont(font3)
        self.summ_3.setStyleSheet(u"font: 16pt \"Cantarell\";")
        self.summ_3.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.transaction_inform)
        self.settings = QWidget()
        self.settings.setObjectName(u"settings")
        self.mnemonic = QLineEdit(self.settings)
        self.mnemonic.setObjectName(u"mnemonic")
        self.mnemonic.setGeometry(QRect(0, 50, 791, 26))
        self.mnemonic.setReadOnly(True)
        self.mnemonic.setClearButtonEnabled(False)
        self.get_mnemonic = QPushButton(self.settings)
        self.get_mnemonic.setObjectName(u"get_mnemonic")
        self.get_mnemonic.setGeometry(QRect(0, 80, 341, 41))
        self.label_14 = QLabel(self.settings)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(340, 20, 101, 18))
        self.label_14.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.settings)
        self.menu_buttons = QGroupBox(self.centralwidget)
        self.menu_buttons.setObjectName(u"menu_buttons")
        self.menu_buttons.setEnabled(False)
        self.menu_buttons.setGeometry(QRect(0, 140, 201, 391))
        self.menu_buttons.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.menu_buttons.setAutoFillBackground(False)
        self.menu_buttons.setStyleSheet(u"border: none;\n"
"")
        self.verticalLayout_3 = QVBoxLayout(self.menu_buttons)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.show_bal = QPushButton(self.menu_buttons)
        self.show_bal.setObjectName(u"show_bal")

        self.verticalLayout_3.addWidget(self.show_bal)

        self.go_to_home = QPushButton(self.menu_buttons)
        self.go_to_home.setObjectName(u"go_to_home")
        font4 = QFont()
        font4.setFamilies([u"Cantarell"])
        font4.setPointSize(11)
        font4.setBold(True)
        font4.setItalic(False)
        self.go_to_home.setFont(font4)
        self.go_to_home.setStyleSheet(u"font: 700 11pt \"Cantarell\";")

        self.verticalLayout_3.addWidget(self.go_to_home)

        self.pushButton_3 = QPushButton(self.menu_buttons)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setEnabled(False)
        icon = QIcon(QIcon.fromTheme(u"emblem-system"))
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setAutoDefault(False)

        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.receive_button = QPushButton(self.menu_buttons)
        self.receive_button.setObjectName(u"receive_button")

        self.verticalLayout_3.addWidget(self.receive_button)

        self.history = QPushButton(self.menu_buttons)
        self.history.setObjectName(u"history")
        icon1 = QIcon(QIcon.fromTheme(u"application-x-executable"))
        self.history.setIcon(icon1)

        self.verticalLayout_3.addWidget(self.history)

        self.contacts = QPushButton(self.menu_buttons)
        self.contacts.setObjectName(u"contacts")
        self.contacts.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.contacts)

        self.setting = QPushButton(self.menu_buttons)
        self.setting.setObjectName(u"setting")

        self.verticalLayout_3.addWidget(self.setting)

        self.change_theme = QPushButton(self.menu_buttons)
        self.change_theme.setObjectName(u"change_theme")

        self.verticalLayout_3.addWidget(self.change_theme)

        self.BalanceFrame = QFrame(self.centralwidget)
        self.BalanceFrame.setObjectName(u"BalanceFrame")
        self.BalanceFrame.setGeometry(QRect(0, 10, 201, 141))
        self.BalanceFrame.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(196, 176, 4);")
        self.verticalLayout_4 = QVBoxLayout(self.BalanceFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.balance_frame = QFrame(self.BalanceFrame)
        self.balance_frame.setObjectName(u"balance_frame")
        self.balance_frame.setStyleSheet(u"border-color: rgb(248, 228, 92);\n"
"border: none;")
        self.verticalLayout = QVBoxLayout(self.balance_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.balance_frame)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.balance = QLabel(self.balance_frame)
        self.balance.setObjectName(u"balance")

        self.verticalLayout.addWidget(self.balance)

        self.label = QLabel(self.balance_frame)
        self.label.setObjectName(u"label")
        self.label.setMouseTracking(False)
        self.label.setStyleSheet(u"border: none;")

        self.verticalLayout.addWidget(self.label)

        self.unconf_balance = QLabel(self.balance_frame)
        self.unconf_balance.setObjectName(u"unconf_balance")
        self.unconf_balance.setStyleSheet(u"border: none;")

        self.verticalLayout.addWidget(self.unconf_balance)


        self.verticalLayout_4.addWidget(self.balance_frame)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(190, 160, 20, 371))
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(4)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton.setDefault(False)
        self.filter_history.setCurrentIndex(-1)
        self.password_ok.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Simple Bitcoin Wallet", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043c\u0430\u0448\u043d\u044f\u044f \u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430", None))
        self.logo.setText("")
        self.author.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0432\u044f\u0437\u044c \u0441 \u0430\u0432\u0442\u043e\u0440\u043e\u043c", None))
        self.docs.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430\u0446\u0438\u044f", None))
        self.source_code.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u0445\u043e\u0434\u043d\u044b\u0439 \u043a\u043e\u0434 (Github)", None))
        self.generate_new_addr.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043d\u043e\u0432\u044b\u0439 \u0430\u0434\u0440\u0435\u0441", None))
        self.address_qr.setText("")
        self.address_label.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0443\u0447\u0435\u043d\u0438\u0435 \u0430\u043a\u0442\u0438\u0432\u043e\u0432", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.address_settings), QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0438\u0439 \u0430\u0434\u0440\u0435\u0441", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.address_viewer), QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435 \u0430\u0434\u0440\u0435\u0441\u0430", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0424\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u0438 (\u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0430 \u0430\u043a\u0442\u0438\u0432\u043e\u0432)", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0440\u0435\u0441 \u043f\u043e\u043b\u0443\u0447\u0430\u0442\u0435\u043b\u044f", None))
#if QT_CONFIG(tooltip)
        self.addr.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.addr.setText("")
        self.addr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0430\u0434\u0440\u0435\u0441 \u043f\u043e\u043b\u0443\u0447\u0430\u0442\u0435\u043b\u044f", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0443\u043c\u043c\u0430 \u043a \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0435", None))
        self.summ.setText("")
        self.summ.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0441\u0443\u043c\u043c\u0443 \u0432 BTC", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043b\u0435\u0435", None))
        ___qtablewidgetitem = self.history_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f", None));
        ___qtablewidgetitem1 = self.history_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0425\u0435\u0448", None));
        ___qtablewidgetitem2 = self.history_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0443\u043c\u043c\u0430", None));
        self.filter_history.setCurrentText("")
        self.load_button.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u0442\u043e\u0440\u0438\u044f \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u0439", None))
        self.password.setText("")
        self.password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.password_ok.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0445\u043e\u0434", None))
        self.check_details.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u044c\u0442\u0435 \u0434\u0435\u0442\u0430\u043b\u0438 \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u0438", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0440\u0435\u0441 \u043f\u043e\u043b\u0443\u0447\u0430\u0442\u0435\u043b\u044f:", None))
        self.address_recipient.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0443\u043c\u043c\u0430 \u043a \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0435:", None))
        self.summ_recipient.setText("")
        self.check_details_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f:", None))
        self.fee_options.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440", None))
        self.fee_options.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0411\u044b\u0441\u0442\u0440\u0430\u044f", None))
        self.fee_options.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u043d\u0434\u0430\u0440\u0442\u043d\u0430\u044f", None))
        self.fee_options.setItemText(3, QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0434\u043b\u0435\u043d\u043d\u0430\u044f", None))

        self.comm.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043c\u0438\u0441\u0441\u0438\u044f (sat/vB):", None))
        self.comission_byte.setText("")
        self.comm_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043c\u0438\u0441\u0441\u0438\u044f \u0437\u0430 \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u044e:", None))
        self.comission_tr.setText("")
        self.push_transaction.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0441\u0442\u0438", None))
        self.cancel_transaction.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u044e", None))
        self.hash.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u043f\u0435\u0448\u043d\u043e! \u0422\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u044f \u043f\u043e\u0434\u043f\u0438\u0441\u0430\u043d\u0430 \u0438 \u043f\u0435\u0440\u0435\u0434\u0430\u043d\u0430 \u0432 \u0441\u0435\u0442\u044c. \u041e\u0436\u0438\u0434\u0430\u0439\u0442\u0435 \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f.", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Coming soon", None))
        self.hash_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.summ_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0445\u043e\u0434\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        ___qtablewidgetitem3 = self.inputs_table.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0440\u0435\u0441", None));
        ___qtablewidgetitem4 = self.inputs_table.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0443\u043c\u043c\u0430", None));
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        ___qtablewidgetitem5 = self.outs_table.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0440\u0435\u0441", None));
        ___qtablewidgetitem6 = self.outs_table.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0443\u043c\u043c\u0430", None));
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043c\u0438\u0441\u0441\u0438\u044f \u0441\u0435\u0442\u0438:", None))
        self.fee.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.summ_3.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u044f", None))
        self.get_mnemonic.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c/\u0441\u043a\u0440\u044b\u0442\u044c \u0441\u0438\u0434-\u0444\u0440\u0430\u0437\u0443 (\u0441\u0435\u043a\u0440\u0435\u0442\u043d\u044b\u0439 \u043a\u043b\u044e\u0447)", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
#if QT_CONFIG(whatsthis)
        self.menu_buttons.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.menu_buttons.setTitle("")
        self.show_bal.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0431\u0430\u043b\u0430\u043d\u0441", None))
        self.go_to_home.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043c\u043e\u0439", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        self.receive_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c", None))
        self.history.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u0442\u043e\u0440\u0438\u044f", None))
        self.contacts.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u044b", None))
        self.setting.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.change_theme.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0442\u0435\u043c\u0443", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0410\u041b\u0410\u041d\u0421", None))
        self.balance.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u043e", None))
        self.unconf_balance.setText("")
    # retranslateUi

