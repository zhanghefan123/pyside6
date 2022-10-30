# 表单布局 -- QFormLayout；主要就是用来管理输入控件及其关联标签的
"""
QFormLayout常用api：
1、addRow() -- 插入行控件
2、insertRow() -- 在指定索引位置插入行控件
3、setWidget() -- 在指定位置插入控件
4、setLayout() -- 在指定位置插入子布局
5、removeRow() -- 删除行
6、labelForField() -- 通过某个控件获取它前面的标签
7、setRowWrapPolicy() -- 设置"行策略"；可设置三个值：QFormLayout.DontWrapRows、QFormLayout.WrapLongRows、QFormLayout.WrapAllRows
8、setFormAlignment()和setLabelAlignment() -- 设置对齐方式；其值都在Qt模块中
9、setHorizontalSpacing()和setVerticalSpacing() -- 设置间距
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
        line_edit1 = QLineEdit()
        line_edit2 = QLineEdit()
        line_edit3 = QLineEdit()
        button = QPushButton('Open')
        box = QFormLayout()

        box.addRow('you_name：', line_edit1)
        box.addRow('age：', line_edit2)
        box.addRow('class：', line_edit3)
        box.setRowWrapPolicy(QFormLayout.WrapLongRows)
        # box.setRowWrapPolicy(QFormLayout.WrapLongRows)
        self.setLayout(box)


if __name__ == '__main__':
    app = QApplication()
    window = Window()
    window.show()
    sys.exit(app.exec())
