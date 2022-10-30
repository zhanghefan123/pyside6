"""
如果槽函数需要传参，有两种方法：
1. 使用lambda表达式
2. 使用偏函数partial

注意：使用以上两种方式传递参数后，会覆盖信号传递给槽的参数
"""
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from functools import partial


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        button = QPushButton('Test')
        button.setCheckable(True)
        box = QHBoxLayout(self)
        box.addWidget(button)

        # button.clicked.connect(self.window_event)
        button.clicked.connect(lambda: self.window_event('hello', 'world'))
        # button.clicked.connect(partial(self.window_event, 'hello'))

    def window_event(self, text, var):
        print(f'this is {var}')
        # pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
