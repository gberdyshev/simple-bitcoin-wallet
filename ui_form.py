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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1026, 533)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(220, 60, 831, 471))
        self.stackedWidget.setLineWidth(3)
        self.stackedWidget.setMidLineWidth(3)
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.stackedWidget.addWidget(self.home)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.stackedWidget.addWidget(self.page_3)
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
        self.pushButton.setGeometry(QRect(80, 180, 191, 71))
        self.pushButton.setCheckable(False)
        self.label = QLabel(self.send)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 120, 761, 20))
        self.stackedWidget.addWidget(self.send)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(10, 140, 181, 41))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 20, 66, 18))
        self.balance = QLabel(self.centralwidget)
        self.balance.setObjectName(u"balance")
        self.balance.setGeometry(QRect(20, 60, 66, 18))
        self.show_bal = QPushButton(self.centralwidget)
        self.show_bal.setObjectName(u"show_bal")
        self.show_bal.setGeometry(QRect(10, 90, 181, 41))
        self.receive_button = QPushButton(self.centralwidget)
        self.receive_button.setObjectName(u"receive_button")
        self.receive_button.setGeometry(QRect(10, 190, 181, 41))
        self.hello = QLabel(self.centralwidget)
        self.hello.setObjectName(u"hello")
        self.hello.setGeometry(QRect(220, 10, 781, 41))
        self.history = QPushButton(self.centralwidget)
        self.history.setObjectName(u"history")
        self.history.setGeometry(QRect(10, 240, 181, 41))
        self.setting = QPushButton(self.centralwidget)
        self.setting.setObjectName(u"setting")
        self.setting.setGeometry(QRect(10, 340, 181, 41))
        self.history_2 = QPushButton(self.centralwidget)
        self.history_2.setObjectName(u"history_2")
        self.history_2.setGeometry(QRect(10, 290, 181, 41))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.addr.setText(QCoreApplication.translate("MainWindow", u"\u0430\u0434\u0440\u0435\u0441", None))
        self.summ.setText(QCoreApplication.translate("MainWindow", u"\u0441\u0443\u043c\u043c\u0430", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        self.label.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0410\u041b\u0410\u041d\u0421", None))
        self.balance.setText("")
        self.show_bal.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0431\u0430\u043b\u0430\u043d\u0441", None))
        self.receive_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c", None))
        self.hello.setText("")
        self.history.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u0442\u043e\u0440\u0438\u044f", None))
        self.setting.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.history_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u044b", None))
    # retranslateUi

