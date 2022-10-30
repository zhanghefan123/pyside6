# 信号（Signals）和槽（Slots）的特性：
"""
1. 一个信号可以绑定多个槽（注：绑定的多个槽的执行顺序根据绑定顺序决定）
2. 一个槽可以被绑定到多个信号
3. 信号可以往槽中传递值（注：为信号传参，参数就会被发送给槽函数）
4. 一个信号可以连接另一个信号
"""
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        button = QPushButton('Ok')
        box = QHBoxLayout()
        box.addWidget(button)
        self.setLayout(box)

        # button.setCheckable(True)

        def window_event(checked):
            print(checked)

        # button.toggled.connect(window_event)
        button.clicked.connect(self.slots2)
        button.clicked.connect(self.slots1)

    def slots1(self):
        print('hello world')

    def slots2(self):
        print('hello Python')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
