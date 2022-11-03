# 关于表单验证① -- 校验器，包含：QIntValidator、QDoubleValidator、QRegularExpressionValidator
# 1. QIntValidator(整数校验器)
"""
QIntValidator常用api：
1、setTop()、setBottom() -- 设置校验器的上限和下限
2、setRange() -- 设置校验值的范围

QIntValidator常用信号：
1、topChanged -- 当校验上限值改变时触发
2、BottomChanged -- 当校验下限值改变时触发
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
        self.line_edit = QLineEdit()
        button = QPushButton('test')
        box = QHBoxLayout()
        box.addWidget(self.line_edit)
        box.addWidget(button)
        self.setLayout(box)

        int_validator = QIntValidator()
        # 设置方式1：
        int_validator.setRange(1, 99) # 输入框之中将只能够输入设置的范围
        # 设置方式2：
        # int_validator.setTop(99) # 进行上限的限制
        # int_validator.setBottom(1) # 进行下限的限制
        self.line_edit.setValidator(int_validator)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
