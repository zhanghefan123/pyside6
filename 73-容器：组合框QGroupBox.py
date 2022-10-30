# QGroupBox -- 组合框；可容纳多个控件，并提供一个标题
"""
QGroupBox常用api：
1、setTitle() -- 设置标题
2、setAlignment() -- 设置标题对齐方式
3、setCheckable() -- 设置勾选可用
4、setFlat() -- 设置是否平面显示
5、title() -- 返回标题文本
6、isFlat() -- 判断是否扁平
7、isChecked() -- 判断是否勾选
8、isCheckable() -- 判断是否支持勾选

QGroupBox信号：
1、clicked -- 标题可勾选是前提，点击标题会触发
2、toggled -- 标题可勾选是前提，标题状态改变会触发（点击、代码修改勾选状态）
"""
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        text_edit = QTextEdit()
        button1 = QPushButton('Ok')
        button2 = QPushButton('Cancel')
        box = QGridLayout()
        box2 = QHBoxLayout()
        box.addWidget(text_edit, 0, 0, 3, 2)
        box.addWidget(button1, 3, 0, 1, 1)
        box.addWidget(button2, 3, 1, 1, 1)

        group_box = QGroupBox()
        # group_box.setFlat(True)
        group_box.setTitle('请填写您的简介：')
        group_box.setCheckable(True)
        # group_box.setChecked(False)
        group_box.setLayout(box)
        box2.addWidget(group_box)

        self.setLayout(box2)

        def do_something():
            group_box.setChecked(False)

        button1.clicked.connect(do_something)
        group_box.clicked.connect(self.window_event)

    def window_event(self):
        print('hello world')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
