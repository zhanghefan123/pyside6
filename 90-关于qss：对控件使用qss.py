# 有哪些控件可以使用qss来设置样式
# 可查询官方文档：https://doc.qt.io/qt-6/stylesheet-reference.html#drop-down-sub

# 注意：能够设置qss的控件，官方文档已经完整列出，没有列出的即无法使用qss，即使为其设置对象名，class属性值，也无法使用qss
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
        self.window_ui()

    def window_ui(self):
        button1 = QPushButton('Ok')
        button2 = QPushButton('Cancel')
        box = QHBoxLayout()
        box.addWidget(button1)
        box.addWidget(button2)
        self.setLayout(box)

        self.setStyleSheet(qss_read('qss1.qss'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
