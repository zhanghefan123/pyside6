# QObject -- qt对象的基类；负责定义qt对象的核心接口，包括：基本信息、行为、核心机制（信号和槽、事件、定时器、翻译等..）
"""
与"信号和槽"相关的主要api：
1、blockSignals() -- 阻止发射信号
2、connect() -- 连接信号和槽
3、disconnect() -- 解除连接信号和槽
4、sender() -- 返回触发信号的对象
"""
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        box = QVBoxLayout(self)
        button = QPushButton('Cancel')
        box.addWidget(button)

        # button.blockSignals(True)

        button.clicked.connect(self.window_event)

    def window_event(self):
        # print('hello python')
        self.sender().setText('Ok')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
