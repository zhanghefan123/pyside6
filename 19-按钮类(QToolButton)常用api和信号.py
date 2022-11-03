# 按钮控件
# 4. QToolButton(工具按钮) 只显示图标，并且可以携带菜单
"""
QToolButton常用api：
1、setMenu() -- 为按钮设置菜单
2、setPopupMode() -- 设置菜单弹出的模式，有三种形式：QToolButton.DelayedPopup(长按才会弹出)、QToolButton.MenuButtonPopup (点击边上按钮弹出)、QToolButton.InstantPopup (点击立即弹出)
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
        self.button2 = QToolButton()
        button3 = QToolButton()
        self.button1.setIcon(QIcon('icons/header1.png'))
        self.button2.setIcon(QIcon('icons/header2.png'))
        button3.setIcon(QIcon('icons/header3.png'))
        self.button1.setIconSize(QSize(30, 30))
        self.button2.setIconSize(QSize(30, 30))
        button3.setIconSize(QSize(30, 30))
        box = QHBoxLayout()
        box.addWidget(self.button1)
        box.addWidget(self.button2)
        box.addWidget(button3)
        self.setLayout(box)
        self.menu = QMenu()
        self.menu.addAction('Open')
        self.menu.addAction('Cancel')
        self.menu.addAction('Save')

        self.button1.setMenu(self.menu)
        self.button1.setPopupMode(QToolButton.DelayedPopup)
        self.button1.setToolButtonStyle(Qt.ToolButtonIconOnly)


        self.button1.triggered.connect(self.button1_triggered)
        self.button1.clicked.connect(self.window_event)
        self.button2.clicked.connect(self.do_something)

    def window_event(self):
        print("hello world")
        # 通过这个方法我们可以判断哪一个action被点击了
        action = self.menu.exec(QCursor.pos())
        print(action.text())

    # 当toolbutton内部的菜单项被点击的时候触发
    def button1_triggered(self, action):
        print(action.text())

    def do_something(self):
        self.button1.click()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
