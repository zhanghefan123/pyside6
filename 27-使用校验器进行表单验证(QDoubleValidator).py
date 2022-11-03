# 关于表单验证① -- 校验器，包含：QIntValidator、QDoubleValidator、QRegularExpressionValidator
# 2. QDoubleValidator(双重校验器)
"""
QDoubleValidator常用api：
1、setTop()、setBottom() -- 设置校验器的上限和下限
2、setRange() -- 设置校验值的范围
3、setDecimals() -- 设置小数点位数
4、setNotation() -- 设置数值的书写形式，有两个值：QDoubleValidator.StandardNotation(以标准数字格式)、QDoubleValidator.ScientificNotation(以科学计数格式)


QDoubleValidator常用信号：
1、topChanged -- 当校验上限值改变时会触发
2、BottomChanged -- 当校验下限值改变时会触发
3、decimalsChanged -- 当小数位数改变时会触发
4、notationChanged -- 当数值的书写形式改变时会触发
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

        d_validator = QDoubleValidator()
        d_validator.setRange(1, 99)
        d_validator.setDecimals(2) # 设置小数点的位数
        self.line_edit.setValidator(d_validator)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
