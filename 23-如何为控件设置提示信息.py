# 为控件添加提示信息 -- setToolTip方法；当鼠标移动到控件上停留一阵后会显示

import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.window_ui()

    def window_ui(self):
        line_edit = QLineEdit()
        button1 = QPushButton('Open')
        button2 = QPushButton('Cancel')
        box = QHBoxLayout()
        box.addWidget(line_edit)
        box.addWidget(button1)
        box.addWidget(button2)
        self.setLayout(box)
        line_edit.setToolTip('this is line..')
        button1.setToolTip('this is open..')

    def window_event(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
