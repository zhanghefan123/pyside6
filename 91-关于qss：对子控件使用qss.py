# 部分控件存在"子控件"，可以为子控件设置qss
# 可查询官方文档：https://doc.qt.io/qt-6/stylesheet-reference.html#drop-down-sub

import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


def qss_read(file):
    with open(file) as f:
        return f.read()


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        box = QHBoxLayout()
        slider = QSlider()
        box.addWidget(slider)
        self.setLayout(box)

        slider.setOrientation(Qt.Horizontal)
        self.setStyleSheet(qss_read('qss1.qss'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
