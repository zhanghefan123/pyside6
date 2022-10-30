# 按钮控件 -- QAbstractButton；这个类是QToolButton、QRadioButton、QPushButton、QCheckBox等按钮类的抽象基类
# 1. QPushButton(普通按钮)
"""
QPushButton常用api：
1、setText() -- 设置按钮上的文本
2、setIcon() -- 为按钮设置图片
3、setIconSize() -- 设置按钮上的图片的尺寸
4、icon()和iconSize() -- 返回按钮上的图片、图片的尺寸；注意，返回的都是对应的对象
5、setCheckable() -- 设置按钮具备"开关"功能（可设置"按下"或"未按下"状态）
6、setChecked() -- 将按钮设置为"按下"状态
7、setDown() -- 将按钮设置为"按下"状态，需要点击两次才能让按钮弹起
8、isChecked()、isDown() -- 判断按钮是否Checked、是否Down
9、click() -- 单击按钮；会触发clicked信号
10、setShortcut() -- 设置快捷键
11、text() -- 返回按钮上的文本
12、setDefault() -- 设置按钮为默认按钮


QPushButton常用信号：
1、clicked -- 按下按钮，并释放后触发
2、pressed -- 当按下按钮就会触发
3、toggled -- 当按钮的状态发生改变时触发
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
        self.button1 = QPushButton('Open')
        self.button2 = QPushButton('Cancel')

        box = QHBoxLayout()
        box.addWidget(self.button1)
        box.addWidget(self.button2)
        self.setLayout(box)

        self.button1.clicked.connect(self.window_event)

    def window_event(self):
        print('hello world')


if __name__ == '__main__':
    app = QApplication()
    window = Window()
    window.show()
    sys.exit(app.exec())
