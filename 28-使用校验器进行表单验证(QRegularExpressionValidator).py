# 关于表单验证① -- 校验器，包含：QIntValidator、QDoubleValidator、QRegularExpressionValidator
# 3. QRegularExpressionValidator(正则校验器)
"""
QRegularExpressionValidator常用api：
1、setRegularExpression() -- 设置"正则表达式"校验
2、validate() -- 返回当前校验器的状态，有三种状态：Invalid、Intermediate、Acceptable


QRegularExpressionValidator常用信号：
1、regularExpressionChanged -- 当校验器中的正则表达式改变时会触发
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
        button = QPushButton('Save')
        box = QHBoxLayout()
        box.addWidget(self.line_edit)
        box.addWidget(button)
        self.setLayout(box)

        self.rex_validator = QRegularExpressionValidator()
        # 允许输入8位的数字
        self.rex_validator.setRegularExpression('\d{8}')
        self.line_edit.setValidator(self.rex_validator)

        self.line_edit.textEdited.connect(self.window_event)
        # button.clicked.connect(self.window_event)

    def window_event(self):
        print(self.rex_validator.validate(self.line_edit.text(), 0))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
