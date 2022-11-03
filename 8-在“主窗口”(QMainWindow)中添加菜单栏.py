# QMainWindow（主窗口类）
# (1)、如何在主窗口中添加菜单栏
"""
1、调用menuBar方法获取到窗口菜单栏
2、addMenu方法用于添加子菜单，addAction方法用于添加菜单项
3、QAction类用于添加"动作" -- 在一个典型的GUI程序中，在用户界面上，常常使用不同的操作方式来完成同一个事情；例如：①菜单里的菜单项，②工具栏中的某个工具，③直接使用快捷键
4、QAction类的一些常用api：

    setIcon() -- 添加图标
    setText() -- 添加文本
    setToolTip() -- 添加提示信息
    setShortcut() -- 设置快捷键
    setCheckable() -- 设置成check选择模式
    setChecked() -- 设置成选中/未选中
"""

import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.window_ui()

    def window_ui(self):
        menu = self.menuBar()
        file_menu = menu.addMenu('文件')
        create = file_menu.addAction('新建...(N)')
        file_menu.addAction(QIcon('icons/file_open.png'), '打开...(O)')

        open_recent = file_menu.addMenu('打开最近')
        open_recent.addAction('管理项目...')
        create.setShortcut(Qt.CTRL + Qt.Key_1)


if __name__ == '__main__':
    app = QApplication()
    window = Window()
    window.show()
    sys.exit(app.exec())
