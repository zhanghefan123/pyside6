# QMenu -- 菜单类,这是右键菜单的时候用到的类，
# 我们需要和我们的QMainWindow之中的菜单栏区分开来
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
9、setActiveAction -- 设置"预激活"的菜单项,让一个action被提前的选中

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
        self.op = self.menu.addAction('Open...') # 添加叶子结点
        self.cancel = self.menu.addMenu('Cancel...') # 添加分枝结点
        self.menu.addSeparator()
        self.yes = self.cancel.addAction('Yes')
        self.cancel.addAction('No')
        self.save = self.menu.addAction('Save...')

        # 当我们点击了menu之中的任意一个action的时候会触发这个事件
        self.menu.triggered.connect(self.window_event)
        # 当我们的鼠标停留在save上的时候会不停的触发这个事件
        # 当我们的鼠标停留在save上的时候会不停的触发这个事件
        self.save.hovered.connect(self.window_event2)

    def window_event2(self):
        print("hover")

    def window_event(self, action):
        print(action.text())
        print('hello world')

    # 要使得我们的菜单在鼠标点击的位置出现要实现这个方法
    def mousePressEvent(self, event):
        # self.menu.setActiveAction(self.save)
        # QCursor.pos() 使得菜单和鼠标的位置一致
        # 这是同步方式，会在这里进行阻塞，，然后当我们点击其中的一个action会返回我们点击的action
        action = self.menu.exec(QCursor.pos())
        print(action.text())


if __name__ == '__main__':
    app = QApplication()
    window = Window()
    window.show()
    sys.exit(app.exec())
