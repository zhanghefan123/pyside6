# QMainWindow（主窗口类）
# (1)、如何在主窗口中添加工具栏
"""
1、调用addToolBar方法创建工具栏，一个窗口中可以容纳多个工具栏
2、addAction方法往工具栏中添加工具按钮；（insertAction方法可往指定的控件索引位置添加工具按钮）
3、调用setIconSize方法设置工具栏图标尺寸

QAction类的一些常用api：

    setIcon() -- 添加图标
    setText() -- 添加文本
    setToolTip() -- 添加提示信息
    setShortcut() -- 设置快捷键
    setCheckable() -- 设置成check选择模式
    setChecked() -- 设置成选中/未选中

QToolBar类的一些常用api：

    addAction()和insertAction() -- 往工具栏中添加按钮
    addSeparator()和insertSeparator() -- 添加分隔符
    addWidget() -- 添加可视化控件
    setMovable(bool) -- 设置工具栏可移动
    setIconSize -- 设置工具栏上的图标的尺寸
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
        tool = self.addToolBar('tool-1')

        h1 = tool.addAction(QIcon('./photo/header1.png'), 'header1')
        tool.addAction(QIcon('./photo/header2.png'), 'header2')
        tool.addAction(QIcon('./photo/header3.png'), 'header3')
        tool.setIconSize(QSize(20, 20))
        tool.setMovable(False)


if __name__ == '__main__':
    app = QApplication()
    window = Window()
    window.show()
    sys.exit(app.exec())
