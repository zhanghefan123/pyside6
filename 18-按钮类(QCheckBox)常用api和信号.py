# 按钮控件
# 3. QCheckBox(复选按钮)
"""
QCheckBox常用api：
1、setTristate() -- 让按钮可以设置"半选中"状态
2、setCheckState() -- 设置按钮状态，有三种：Qt.PartiallyChecked、Qt.Unchecked、Qt.Checked
3、isTristate() -- 判断按钮状态是否为半选中
4、checkState() -- 返回按钮当前的状态

QCheckBox常用信号：
1、stateChanged -- 当按钮状态发生改变时会触发
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
        label = QLabel('课余时间你都喜欢做什么：')
        button1 = QCheckBox('看书')
        button2 = QCheckBox('编程')
        button3 = QCheckBox('打篮球')
        button4 = QCheckBox('抓紧时间睡觉...')

        box = QGridLayout()
        box.addWidget(label, 0, 0)
        box.addWidget(button1, 1, 0)
        box.addWidget(button2, 2, 0)
        box.addWidget(button3, 3, 0)
        box.addWidget(button4, 4, 0)
        self.setLayout(box)

        button1.setTristate(True)
        button1.setCheckState(Qt.Checked)
        button1.stateChanged.connect(self.window_event)

    def window_event(self):
        print('hello world')


if __name__ == '__main__':
    app = QApplication()
    window = Window()
    window.show()
    sys.exit(app.exec())
