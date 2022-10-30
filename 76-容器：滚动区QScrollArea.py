# QScrollArea -- 滚动区
"""
QScrollArea常用api：
1、setAlignment() -- 设置控件在滚动区中的对齐方式
2、setWidget() -- 设置滚动区中的控件
3、setWidgetResizable() -- 设置滚动区是否应调整内部控件的大小
4、takeWidget() -- 删除滚动区中的控件
"""
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class my_widget(QWidget):
    def __init__(self):
        super(my_widget, self).__init__()
        box = QVBoxLayout()
        for i in range(100):
            button = QPushButton('Test')
            box.addWidget(button)
        self.setLayout(box)


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        w = my_widget()
        box = QHBoxLayout()
        box.addWidget(w)
        # a = QScrollArea()
        # a.setWidget(w)
        # box.addWidget(a)
        self.setLayout(box)

        # a.setAlignment(Qt.AlignCenter)
        # a.setWidgetResizable(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
