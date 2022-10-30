# 按钮控件
# 2. QRadioButton(单选按钮)
"""
注意事项：单选按钮是一种多选一的机制，同属于一个父窗口中的单选按钮之间是“互斥”的关系
使用QButtonGroup类为按钮分组，调用分组的addButton()将按钮添加到分组中，所属不同组的按钮不会互斥

QPushButton常用信号：
1、toggled -- 当按钮状态发生改变时会触发
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
        self.button1 = QRadioButton('满意')
        self.button2 = QRadioButton('一般')
        self.button3 = QRadioButton('较差')
        self.button4 = QRadioButton('满意')
        self.button5 = QRadioButton('一般')
        self.button6 = QRadioButton('较差')
        label1 = QLabel('专业技能：')
        label2 = QLabel('服务态度：')
        box = QGridLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()

        box.addWidget(label1, 0, 0)
        box.addWidget(label2, 2, 0)
        hbox1.addWidget(self.button1)
        hbox1.addWidget(self.button2)
        hbox1.addWidget(self.button3)
        hbox2.addWidget(self.button4)
        hbox2.addWidget(self.button5)
        hbox2.addWidget(self.button6)
        box.addLayout(hbox1, 1, 0, 1, 3)
        box.addLayout(hbox2, 3, 0, 1, 3)
        self.setLayout(box)

        group1 = QButtonGroup(self)
        group2 = QButtonGroup(self)
        group1.addButton(self.button1)
        group1.addButton(self.button2)
        group1.addButton(self.button3)
        group2.addButton(self.button4)
        group2.addButton(self.button5)
        group2.addButton(self.button6)



        self.button1.setChecked(True)


if __name__ == '__main__':
    app = QApplication()
    window = Window()
    window.show()
    sys.exit(app.exec())
