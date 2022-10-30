# Qt中，用于处理事件的机制 -- 信号与槽
# 什么是事件 -- 程序接收到的"请求"，会产生事件的情况主要有两种：①、在与用户交互中产生的；②、系统自发产生的

"""
Qt中用于处理事件的第一套机制：信号和槽（主要用于处理和用户交互时产生的事件）

1、什么是信号 -- 由接收到"请求"的控件或者动作发出
2、什么是槽 -- 可由开发者来编写的api
3、信号和槽如何绑定用于处理事件呢？ -- 使用信号调用connect方法
"""

import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.window_ui()

    def window_ui(self):
        button = QPushButton('Open')
        box = QHBoxLayout()
        box.addWidget(button)
        self.setLayout(box)

        button.clicked.connect(self.window_event)

    def window_event(self):
        print('hello world')


if __name__ == '__main__':
    app = QApplication()
    window = Window()
    window.show()
    sys.exit(app.exec())
