# 自定义信号有什么好处：
"""
1. 可以使信号传送任何你想传递给槽的数据
2. 可以任意定义触发信号的时机
"""
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class myButton(QPushButton):
    getText = Signal(str)

    def __init__(self, text):
        super(myButton, self).__init__(text)
        self.clicked.connect(self.send_)

    def send_(self):
        self.getText.emit(self.text())


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        button1 = QPushButton('Test')
        button2 = myButton('Ok')
        button3 = myButton('Cancel')
        box = QVBoxLayout(self)
        box.addWidget(button1)
        box.addWidget(button2)
        box.addWidget(button3)

        def window_event(text):
            # button1.setText(button3.text())
            button1.setText(text)

        button2.getText.connect(window_event)
        button3.getText.connect(window_event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
