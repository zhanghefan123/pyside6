# QAction -- "动作"类(官方文档中翻译成"操作")
"""
QAction常用api：
1、setText() -- 设置文本
2、setIcon() -- 设置图片
3、setCheckable() -- 设置动作可勾选
4、setEnabled() -- 设置动作是否可用
5、setFont() -- 设置动作上的字体
6、setChecked() -- 设置动作被勾选
7、setShortcut() -- 设置快捷键
8、text() -- 返回动作的文本
9、isCheckable()、isChecked()、isEnabled() -- 判断是否可勾选、是否被勾选、是否可用


QAction类常用信号：
1、hovered -- 当鼠标移动到此动作上时，或者离开动作时会触发
2、enabledChanged -- 当此动作的可用状态改变时触发
3、triggered -- 当鼠标单击此动作（无论该动作处于菜单栏中还是工具栏中），或使用快捷键时均会触发
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
        op = QAction('Open...', self)
        self.menu.addAction(op)
        cancel = self.menu.addAction('Cancel...')
        save = self.menu.addAction('Save...')
        # cancel.setCheckable(True)
        # cancel.setEnabled(False)
        op.setShortcut(Qt.CTRL + Qt.Key_1, 1)

    def mousePressEvent(self, event):
        self.menu.exec(QCursor.pos())


if __name__ == '__main__':
    app = QApplication()
    window = Window()
    window.show()
    sys.exit(app.exec())
