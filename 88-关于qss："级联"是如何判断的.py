# 在多个位置设置了多个qss样式，qt是如何判断哪些qss是有效（会生效）的？
# qss的"级联"
"""
1、可以设置qss的位置有三个：
    app -- qss的作用范围是app中的所有控件
    窗口（QWidget） -- qss的作用范围是这个窗口中的所有控件
    控件本身 -- qss的作用范围是这个控件

2、优先级：控件 > 窗口 > app

注意：无论在哪里设置qss，也都使用setStyleSheet方法；如果要在app上添加qss，必须使用外部加载方式
"""
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


def qss_read(file):
    with open(file) as f:
        return f.read()


class Win2(QWidget):
    def __init__(self):
        super(Win2, self).__init__()
        button = QPushButton('Test..')
        box = QHBoxLayout(self)
        box.addWidget(button)


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        button1 = QPushButton('Python')
        button2 = QPushButton('Java')
        button3 = QPushButton('C++')
        box = QHBoxLayout(self)
        box.addWidget(button1)
        box.addWidget(button2)
        box.addWidget(button3)

        # self.setStyleSheet('color:red')
        # button1.setStyleSheet('color:red')

        button3.clicked.connect(self.window_event)

    def window_event(self):
        win2 = Win2()
        win2.show()
        win2.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    # app.setStyleSheet(qss_read('test.css'))
    window.show()
    sys.exit(app.exec())
