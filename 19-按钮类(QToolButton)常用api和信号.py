# 按钮控件
# 4. QToolButton(工具按钮)
"""
QToolButton常用api：
1、setMenu() -- 为按钮设置菜单
2、setPopupMode() -- 设置菜单弹出的模式，有三种形式：QToolButton.DelayedPopup、QToolButton.MenuButtonPopup、QToolButton.InstantPopup
3、setToolButtonStyle() -- 设置按钮样式，有几种：Qt.ToolButtonIconOnly(只显示图标)、Qt.ToolButtonTextOnly(只显示文本)、Qt.ToolButtonTextBesideIcon(文字在图标旁)、Qt.ToolButtonTextUnderIcon(文字在图标下)
4、showMenu() -- 显示菜单
5、menu() -- 返回按钮附带的菜单

QToolButton常用信号：
1、clicked -- 单击按钮时会触发
2、triggered -- 点击按钮附带的菜单上的菜单项时会触发
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
        self.button1 = QToolButton()
        button2 = QToolButton()
        button3 = QToolButton()
        self.button1.setIcon(QIcon('./photo/header1.png'))
        button2.setIcon(QIcon('./photo/header2.png'))
        button3.setIcon(QIcon('./photo/header3.png'))
        self.button1.setIconSize(QSize(30, 30))
        button2.setIconSize(QSize(30, 30))
        button3.setIconSize(QSize(30, 30))
        box = QHBoxLayout()
        box.addWidget(self.button1)
        box.addWidget(button2)
        box.addWidget(button3)
        self.setLayout(box)
        # self.menu = QMenu()
        # self.menu.addAction('Open')
        # self.menu.addAction('Cancel')
        # self.menu.addAction('Save')
        #
        # self.button1.setMenu(self.menu)
        # self.button1.setPopupMode(QToolButton.MenuButtonPopup)
        # self.button1.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.button1.triggered.connect(self.window_event)
        button2.clicked.connect(self.do_something)

    def window_event(self):
        print(self.sender().menu())

    def do_something(self):
        self.button1.click()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
