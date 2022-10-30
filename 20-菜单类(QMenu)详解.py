# QMenu -- 菜单类
"""
QMenu常用api：
1、addAction -- 添加"动作"（菜单项）
2、addMenu -- 添加子菜单
3、actions() -- 返回一个由菜单中所有QAction对象组成的列表
4、addSection()、addSeparator() -- 添加分隔线
5、clear() -- 清除所有菜单项
6、removeAction() -- 删除某个菜单项
7、exec(pos) -- 以同步的方式显示菜单；可接收QPoint用于指定菜单出现的位置，常用的有QCursor.pos()和somewidget.mapToGlobal(QPoint(0, 0))
8、popup(pos) -- 以异步的方式显示菜单；参数与exec方法相同
9、setActiveAction -- 设置"预激活"的菜单项

QMenu常用信号：
1、triggered -- 当单击菜单项时会触发
2、hovered -- 当鼠标进入菜单区域时，或者离开菜单区域时都会触发
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
        self.menu = QMenu()
        self.op = self.menu.addAction('Open...')
        cancel = self.menu.addMenu('Cancel...')
        # self.menu.addSeparator()
        self.yes = cancel.addAction('Yes')
        cancel.addAction('No')
        self.save = self.menu.addAction('Save...')

        # self.menu.triggered.connect(self.window_event)
        # self.save.hovered.connect(self.window_event)

    def window_event(self):
        print('hello world')

    def mousePressEvent(self, event):
        # self.menu.setActiveAction(self.save)
        action = self.menu.exec(QCursor.pos())
        # print(action.text())


if __name__ == '__main__':
    app = QApplication()
    window = Window()
    window.show()
    sys.exit(app.exec())
