# 栅格布局 -- QGridLayout；一种丰富的多格布局形式
"""
QGridLayout常用api：
1、addWidget() -- 添加控件
注意：
    (1). 如果添加控件时，控件占据了多行或者多列，则当布局变大或变小时，控件也将维持此比例
    (2). 布局中的行高和列宽的最大值取决于该行或该列中最大的控件的尺寸
    (3). 如果为布局中的控件设置了固定尺寸，则当布局变大或变小时，控件尺寸不会改变
    (4). 如果前面的控件占据了多行或者多列，后面的控件要避免占用前面控件使用到的单元格，否则会发生控件重叠的情况

2、addLayout() -- 添加子布局
3、setColumnMinimumWidth() -- 设置列的最小宽度
4、setRowMinimumHeight() -- 设置行的最小高度
5、setHorizontalSpacing() -- 设置水平间距
6、setVerticalSpacing() -- 设置垂直间距
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
        # 我们在进行gridlayout的创建的时候不需要进行几行几列的指定，他会进行自动的指定。
        box = QGridLayout()
        self.button1 = QPushButton('Open')
        self.button2 = QPushButton('Cancel')
        self.button3 = QPushButton('Save')
        line_edit = QLineEdit()
        # line_edit.setFixedWidth(200)
        # self.button1.setFixedWidth(200)

        # box.addWidget(line_edit, 0, 0)
        # 第一个参数是控件，第二个参数是行，第三个参数是列，然后第三个参数是rowspan(即行占多少)，第四个参数是colspan(即列占多少)
        box.addWidget(self.button1, 0, 0)  # 左上角在第0行第0列，占1行1列
        box.addWidget(self.button2, 0, 1, 1, 2)  # 左上角在第0行第1列，占1行2列
        box.addWidget(self.button3, 0, 3, 1, 2)  # 左上角在第0行第3列，占1行2列
        # box.addWidget(self.button3, 1, 2)

        self.setLayout(box)
        self.button1.clicked.connect(self.window_event)

    def window_event(self):
        pass


if __name__ == '__main__':
    app = QApplication()
    window = Window()
    window.show()
    sys.exit(app.exec())
