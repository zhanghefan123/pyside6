# 关于表单验证② -- setInputMask()
# 通过设置"掩码"，以某种约定好的格式限制用户的输入

"""
掩码符号与说明：

A -- ASCII字母字符是必须输入的a-z、A-Z
a -- ASCII字母字符是允许输入的，不是必须输入的a-z、A-Z
N -- ASCII字母字符是必须输入的a-z、A-Z、0-9
n -- ASCII字母字符是允许输入的，不是必须输入的a-z、A-Z、0-9
X -- 任何字符都是必须输入的
x -- 任何字符都是允许输入的，但不是必须的
9 -- ASCII数字字符是必须输入的0-9
0 -- ASCII数字字符是允许输入的，不是必须输入的0-9
D -- ASCII数字字符是必须输入的1-9
d -- ASCII数字字符是允许输入的，不是必须输入的1-9
# -- 数字字符或者加减符号是允许输入的，但不是必须的
H -- 十六进制格式字符是必须输入的A-F、a-f、0-9
h -- 十六进制格式字符是允许输入的，但不是必须输入的A-F、a-f、0-9
B -- 二进制格式字符是必须输入的(0，1)
b -- 二进制格式字符是允许输入的，但不是必须的(0，1)
> -- 所有的字母字符都大写
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
        line_edit1 = QLineEdit()
        button1 = QPushButton('GO')
        box = QHBoxLayout()
        box.addWidget(line_edit1)
        # box.addWidget(line_edit2)
        box.addWidget(button1)
        line_edit1.setPlaceholderText('测试用')
        self.setLayout(box)

        line_edit1.setInputMask('AAAAAA')
        line_edit1.returnPressed.connect(self.window_event)

    def window_event(self):
        print('hello world')


if __name__ == '__main__':
    app = QApplication()
    window = Window()
    window.show()
    sys.exit(app.exec())
