import asyncio
from PySide6 import QtWidgets
from asyncslot import asyncSlot, AsyncSlotRunner

async def say_hi():
    await asyncio.sleep(1)
    QtWidgets.QMessageBox.information(None, "Demo", "Hi")

app = QtWidgets.QApplication()
button = QtWidgets.QPushButton()
button.setText('Say Hi after one second')
button.clicked.connect(asyncSlot(say_hi))  # <-- instead of connect(say_hi)
button.show()

with AsyncSlotRunner():  # <-- wrap in Runner
    app.exec()

