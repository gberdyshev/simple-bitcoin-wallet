# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'firstrun_form.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(614, 404)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 10, 611, 391))
        self.welcome = QWidget()
        self.welcome.setObjectName(u"welcome")
        self.create_wallet = QPushButton(self.welcome)
        self.create_wallet.setObjectName(u"create_wallet")
        self.create_wallet.setGeometry(QRect(170, 60, 251, 121))
        self.import_wallet = QPushButton(self.welcome)
        self.import_wallet.setObjectName(u"import_wallet")
        self.import_wallet.setGeometry(QRect(170, 190, 251, 91))
        self.stackedWidget.addWidget(self.welcome)
        self.importer = QWidget()
        self.importer.setObjectName(u"importer")
        self.private_key_2 = QLineEdit(self.importer)
        self.private_key_2.setObjectName(u"private_key_2")
        self.private_key_2.setGeometry(QRect(20, 40, 571, 26))
        self.check = QPushButton(self.importer)
        self.check.setObjectName(u"check")
        self.check.setGeometry(QRect(20, 80, 181, 41))
        self.public_key_2 = QLineEdit(self.importer)
        self.public_key_2.setObjectName(u"public_key_2")
        self.public_key_2.setGeometry(QRect(20, 150, 571, 26))
        self.address_2 = QLineEdit(self.importer)
        self.address_2.setObjectName(u"address_2")
        self.address_2.setGeometry(QRect(20, 200, 571, 26))
        self.line_open = QLabel(self.importer)
        self.line_open.setObjectName(u"line_open")
        self.line_open.setGeometry(QRect(20, 130, 121, 18))
        self.label_5 = QLabel(self.importer)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 180, 121, 18))
        self.finish_import = QPushButton(self.importer)
        self.finish_import.setObjectName(u"finish_import")
        self.finish_import.setGeometry(QRect(410, 340, 181, 41))
        self.stackedWidget.addWidget(self.importer)
        self.creator = QWidget()
        self.creator.setObjectName(u"creator")
        self.private_key = QLineEdit(self.creator)
        self.private_key.setObjectName(u"private_key")
        self.private_key.setGeometry(QRect(10, 50, 581, 26))
        self.public_key = QLineEdit(self.creator)
        self.public_key.setObjectName(u"public_key")
        self.public_key.setGeometry(QRect(10, 130, 581, 26))
        self.address = QLineEdit(self.creator)
        self.address.setObjectName(u"address")
        self.address.setGeometry(QRect(10, 210, 571, 26))
        self.label = QLabel(self.creator)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 121, 18))
        self.label_2 = QLabel(self.creator)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 110, 121, 18))
        self.label_3 = QLabel(self.creator)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 180, 121, 18))
        self.generate = QPushButton(self.creator)
        self.generate.setObjectName(u"generate")
        self.generate.setGeometry(QRect(400, 320, 191, 51))
        self.show_private_key = QPushButton(self.creator)
        self.show_private_key.setObjectName(u"show_private_key")
        self.show_private_key.setEnabled(False)
        self.show_private_key.setGeometry(QRect(140, 320, 221, 51))
        self.show_private_key.setCheckable(False)
        self.show_private_key.setFlat(False)
        self.go = QPushButton(self.creator)
        self.go.setObjectName(u"go")
        self.go.setEnabled(False)
        self.go.setGeometry(QRect(400, 250, 191, 51))
        self.warning_label = QLabel(self.creator)
        self.warning_label.setObjectName(u"warning_label")
        self.warning_label.setGeometry(QRect(20, 250, 351, 61))
        self.stackedWidget.addWidget(self.creator)
        self.password_creator = QWidget()
        self.password_creator.setObjectName(u"password_creator")
        self.stackedWidget.addWidget(self.password_creator)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.create_wallet.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043a\u043e\u0448\u0435\u043b\u0435\u043a", None))
        self.import_wallet.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u043f\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043a\u043e\u0448\u0435\u043b\u0435\u043a", None))
        self.private_key_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0442\u0430\u0432\u044c\u0442\u0435 \u0432\u0430\u0448 \u0441\u0435\u043a\u0440\u0435\u0442\u043d\u044b\u0439 \u043a\u043b\u044e\u0447", None))
        self.check.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c", None))
        self.line_open.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044b\u0439 \u043a\u043b\u044e\u0447", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0440\u0435\u0441", None))
        self.finish_import.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u043f\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u043a\u0440\u0435\u0442\u043d\u044b\u0439 \u043a\u043b\u044e\u0447", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044b\u0439 \u043a\u043b\u044e\u0447", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0440\u0435\u0441", None))
        self.generate.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.show_private_key.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0441\u0435\u043a\u0440\u0435\u0442\u043d\u044b\u0439 \u043a\u043b\u044e\u0447", None))
        self.go.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0439\u0442\u0438 \u043a \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u044e", None))
        self.warning_label.setText("")
    # retranslateUi

