"""
Simple Bitcoin Wallet
GNU GPL v3
Development and distribution: Grigoriy Berdyshev
Technical Сonsultant: Oleg Akhmadeev
2023-2024
"""
import sys

# Импорт классов, соответствующих окнам приложения
from simple_bitcoin_wallet.classes.FirstRunWindow import FirstRunWindow
from simple_bitcoin_wallet.classes.MainWindow import MainWindow

from simple_bitcoin_wallet.scripts.database import Database

from PySide6.QtWidgets import QApplication, QMainWindow

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.w1 = FirstRunWindow() #окно первоначальной настройки
    def show_w1(self):

        self.w1 = FirstRunWindow()
        self.w1.setFixedSize(666, 441)
        self.w1.ui.confirm.clicked.connect(self.show_w2)
        self.w1.ui.confirm.clicked.connect(self.w1.close)

        self.w1.show()

    def show_w2(self):
        self.w2 = MainWindow() # основное окно приложения
        self.w2.setFixedSize(1026, 533)
        self.w2.show()
 
 
def main():
    app = QApplication(sys.argv)
    widget = Main()
    if Database().init_app(): # при наличии ключей запускается сразу MainWindow
        widget.show_w2()
    else:
        widget.show_w1() # при отсутствии ключей запускается мастер первоначальной настройки
    sys.exit(app.exec())

if __name__ == "__main__":
    main()