# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'firstrun_form.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QLabel, QLineEdit, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(666, 441)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 10, 661, 451))
        self.welcome = QWidget()
        self.welcome.setObjectName(u"welcome")
        self.widget = QWidget(self.welcome)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(150, 70, 361, 261))
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.create_wallet = QPushButton(self.widget)
        self.create_wallet.setObjectName(u"create_wallet")

        self.verticalLayout_4.addWidget(self.create_wallet)

        self.import_wallet = QPushButton(self.widget)
        self.import_wallet.setObjectName(u"import_wallet")

        self.verticalLayout_4.addWidget(self.import_wallet)

        self.stackedWidget.addWidget(self.welcome)
        self.importer = QWidget()
        self.importer.setObjectName(u"importer")
        self.importer_frame_2 = QFrame(self.importer)
        self.importer_frame_2.setObjectName(u"importer_frame_2")
        self.importer_frame_2.setGeometry(QRect(20, 0, 621, 431))
        self.finish_import_2 = QPushButton(self.importer_frame_2)
        self.finish_import_2.setObjectName(u"finish_import_2")
        self.finish_import_2.setEnabled(False)
        self.finish_import_2.setGeometry(QRect(0, 400, 621, 26))
        font = QFont()
        font.setBold(True)
        self.finish_import_2.setFont(font)
        self.finish_import_2.setCheckable(False)
        self.finish_import_2.setAutoDefault(False)
        self.importer_frame_3 = QFrame(self.importer_frame_2)
        self.importer_frame_3.setObjectName(u"importer_frame_3")
        self.importer_frame_3.setGeometry(QRect(0, 1, 621, 391))
        self._2 = QVBoxLayout(self.importer_frame_3)
        self._2.setObjectName(u"_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.import_opt_frame_2 = QFrame(self.importer_frame_3)
        self.import_opt_frame_2.setObjectName(u"import_opt_frame_2")
        self.import_opt_frame = QVBoxLayout(self.import_opt_frame_2)
        self.import_opt_frame.setObjectName(u"import_opt_frame")
        self.import_options = QComboBox(self.import_opt_frame_2)
        self.import_options.addItem("")
        self.import_options.addItem("")
        self.import_options.addItem("")
        self.import_options.setObjectName(u"import_options")
        self.import_options.setEnabled(True)
        self.import_options.setEditable(False)

        self.import_opt_frame.addWidget(self.import_options)

        self.private_key_2 = QLineEdit(self.import_opt_frame_2)
        self.private_key_2.setObjectName(u"private_key_2")
        self.private_key_2.setEnabled(False)
        self.private_key_2.setAutoFillBackground(False)
        self.private_key_2.setFrame(True)
        self.private_key_2.setReadOnly(False)
        self.private_key_2.setClearButtonEnabled(True)

        self.import_opt_frame.addWidget(self.private_key_2)

        self.mnemonic_2 = QLineEdit(self.import_opt_frame_2)
        self.mnemonic_2.setObjectName(u"mnemonic_2")
        self.mnemonic_2.setEnabled(False)
        self.mnemonic_2.setClearButtonEnabled(True)

        self.import_opt_frame.addWidget(self.mnemonic_2)

        self.check = QPushButton(self.import_opt_frame_2)
        self.check.setObjectName(u"check")
        self.check.setFont(font)

        self.import_opt_frame.addWidget(self.check)


        self.verticalLayout_3.addWidget(self.import_opt_frame_2)

        self.addr_frame_2 = QFrame(self.importer_frame_3)
        self.addr_frame_2.setObjectName(u"addr_frame_2")
        self.addr_frame = QVBoxLayout(self.addr_frame_2)
        self.addr_frame.setSpacing(1)
        self.addr_frame.setObjectName(u"addr_frame")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.line_open = QLabel(self.addr_frame_2)
        self.line_open.setObjectName(u"line_open")

        self.verticalLayout.addWidget(self.line_open)

        self.public_key_2 = QLineEdit(self.addr_frame_2)
        self.public_key_2.setObjectName(u"public_key_2")
        self.public_key_2.setReadOnly(True)

        self.verticalLayout.addWidget(self.public_key_2)


        self.addr_frame.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(self.addr_frame_2)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.address_2 = QLineEdit(self.addr_frame_2)
        self.address_2.setObjectName(u"address_2")
        self.address_2.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.address_2)

        self.finish_import = QPushButton(self.addr_frame_2)
        self.finish_import.setObjectName(u"finish_import")
        self.finish_import.setEnabled(True)
        self.finish_import.setFont(font)
        self.finish_import.setTabletTracking(False)
        self.finish_import.setCheckable(False)
        self.finish_import.setAutoDefault(False)

        self.verticalLayout_2.addWidget(self.finish_import)

        self.import_progress = QProgressBar(self.addr_frame_2)
        self.import_progress.setObjectName(u"import_progress")
        self.import_progress.setValue(0)

        self.verticalLayout_2.addWidget(self.import_progress)


        self.addr_frame.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addWidget(self.addr_frame_2)


        self._2.addLayout(self.verticalLayout_3)

        self.stackedWidget.addWidget(self.importer)
        self.creator = QWidget()
        self.creator.setObjectName(u"creator")
        self.warning_label = QLabel(self.creator)
        self.warning_label.setObjectName(u"warning_label")
        self.warning_label.setGeometry(QRect(10, 250, 361, 61))
        self.layoutWidget = QWidget(self.creator)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 631, 281))
        self.creator_fr = QVBoxLayout(self.layoutWidget)
        self.creator_fr.setObjectName(u"creator_fr")
        self.creator_fr.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.creator_fr.addWidget(self.label_6)

        self.mnemonic = QLineEdit(self.layoutWidget)
        self.mnemonic.setObjectName(u"mnemonic")
        self.mnemonic.setEchoMode(QLineEdit.Password)
        self.mnemonic.setReadOnly(True)

        self.creator_fr.addWidget(self.mnemonic)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.creator_fr.addWidget(self.label)

        self.private_key = QLineEdit(self.layoutWidget)
        self.private_key.setObjectName(u"private_key")
        self.private_key.setEchoMode(QLineEdit.Password)
        self.private_key.setReadOnly(True)

        self.creator_fr.addWidget(self.private_key)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.creator_fr.addWidget(self.label_2)

        self.public_key = QLineEdit(self.layoutWidget)
        self.public_key.setObjectName(u"public_key")
        self.public_key.setReadOnly(True)

        self.creator_fr.addWidget(self.public_key)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.creator_fr.addWidget(self.label_3)

        self.address = QLineEdit(self.layoutWidget)
        self.address.setObjectName(u"address")
        self.address.setReadOnly(True)

        self.creator_fr.addWidget(self.address)

        self.layoutWidget1 = QWidget(self.creator)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(240, 310, 401, 121))
        self.gridLayout = QGridLayout(self.layoutWidget1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.show_private_key = QPushButton(self.layoutWidget1)
        self.show_private_key.setObjectName(u"show_private_key")
        self.show_private_key.setEnabled(False)

        self.gridLayout.addWidget(self.show_private_key, 0, 0, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.go = QPushButton(self.layoutWidget1)
        self.go.setObjectName(u"go")
        self.go.setEnabled(False)

        self.verticalLayout_5.addWidget(self.go)

        self.generate = QPushButton(self.layoutWidget1)
        self.generate.setObjectName(u"generate")

        self.verticalLayout_5.addWidget(self.generate)


        self.gridLayout.addLayout(self.verticalLayout_5, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.creator)
        self.password_creator = QWidget()
        self.password_creator.setObjectName(u"password_creator")
        self.label_4 = QLabel(self.password_creator)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 371, 18))
        self.password = QLineEdit(self.password_creator)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(20, 40, 331, 26))
        self.password.setEchoMode(QLineEdit.Password)
        self.confirm = QPushButton(self.password_creator)
        self.confirm.setObjectName(u"confirm")
        self.confirm.setGeometry(QRect(390, 340, 211, 41))
        self.stackedWidget.addWidget(self.password_creator)
        self.importer_from_seed = QWidget()
        self.importer_from_seed.setObjectName(u"importer_from_seed")
        self.mnemonic_import = QLineEdit(self.importer_from_seed)
        self.mnemonic_import.setObjectName(u"mnemonic_import")
        self.mnemonic_import.setGeometry(QRect(10, 50, 631, 26))
        self.mnemonic_import.setEchoMode(QLineEdit.Password)
        self.mnemonic_import.setReadOnly(True)
        self.label_7 = QLabel(self.importer_from_seed)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 20, 161, 18))
        self.pushButton = QPushButton(self.importer_from_seed)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 90, 191, 51))
        self.pushButton_2 = QPushButton(self.importer_from_seed)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(250, 370, 191, 51))
        self.pushButton_3 = QPushButton(self.importer_from_seed)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(450, 370, 191, 51))
        self.stackedWidget.addWidget(self.importer_from_seed)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.import_options.setCurrentIndex(0)
        self.finish_import.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Simple Bitcoin Wallet (Setup)", None))
        self.create_wallet.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043a\u043e\u0448\u0435\u043b\u0435\u043a", None))
        self.import_wallet.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u043f\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043a\u043e\u0448\u0435\u043b\u0435\u043a", None))
        self.finish_import_2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0435\u0440\u0448\u0438\u0442\u044c", None))
        self.import_options.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0412\u0430\u0440\u0438\u0430\u043d\u0442 \u0438\u043c\u043f\u043e\u0440\u0442\u0430", None))
        self.import_options.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0421\u0435\u043a\u0440\u0435\u0442\u043d\u044b\u0439 \u043a\u043b\u044e\u0447", None))
        self.import_options.setItemText(2, QCoreApplication.translate("MainWindow", u"\u041c\u043d\u0435\u043c\u043e\u043d\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u0444\u0440\u0430\u0437\u0430", None))

        self.private_key_2.setText("")
        self.private_key_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0442\u0430\u0432\u044c\u0442\u0435 \u0432\u0430\u0448 \u0441\u0435\u043a\u0440\u0435\u0442\u043d\u044b\u0439 \u043a\u043b\u044e\u0447", None))
        self.mnemonic_2.setText("")
        self.mnemonic_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0442\u0430\u0432\u044c\u0442\u0435 \u0432\u0430\u0448\u0435 \u043c\u043d\u0435\u043c\u043e\u043d\u0438\u0447\u0435\u0441\u043a\u0443\u044e \u0444\u0440\u0430\u0437\u0443", None))
        self.check.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c", None))
        self.line_open.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044b\u0439 \u043a\u043b\u044e\u0447", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0440\u0435\u0441", None))
        self.finish_import.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u043f\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.warning_label.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043d\u0435\u043c\u043e\u043d\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u0444\u0440\u0430\u0437\u0430", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u043a\u0440\u0435\u0442\u043d\u044b\u0439 \u043a\u043b\u044e\u0447", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044b\u0439 \u043a\u043b\u044e\u0447", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0440\u0435\u0441", None))
        self.show_private_key.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0441\u0435\u043a\u0440\u0435\u0442\u043d\u044b\u0439 \u043a\u043b\u044e\u0447", None))
        self.go.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0439\u0442\u0438 \u043a \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u044e", None))
        self.generate.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u0439\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c \u0434\u043b\u044f \u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u0438\u044f \u0432\u0430\u0448\u0435\u0433\u043e \u043a\u043e\u0448\u0435\u043b\u044c\u043a\u0430", None))
        self.confirm.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0439\u0442\u0438 \u043a \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u044e", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043d\u0435\u043c\u043e\u043d\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u0444\u0440\u0430\u0437\u0430", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u043f\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0435\u0440\u0448\u0438\u0442\u044c", None))
    # retranslateUi

