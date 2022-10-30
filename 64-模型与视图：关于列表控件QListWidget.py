# QListWidget -- 列表控件
"""
QListWidget常用api：
1、addItem() -- 添加项目；（注意：项目类型为QListWidgetItem）
2、addItems() -- 添加多个项目
3、count() -- 返回列表项数目
4、currentItem()、currentRow() -- 返回当前所选的项目，返回当前所选的行号
5、indexFromItem() -- 通过指定的项目返回QModelIndex
6、itemFromIndex() -- 通过指定的QModelIndex返回项目
7、insertItem()、insertItems() -- 在指定位置插入项目
8、item() -- 返回指定行的项目
9、row() -- 返回指定项目所在的行
10、takeItem() -- 删除指定的行，并将此行中的项目返回，类型是QListWidgetItem
11、setCurrentItem()、setCurrentRow() -- 设置当前选定的项目、当前选中的行


QListWidget常用信号：
1、currentItemChanged -- 所选项目改变时会触发（无论使用鼠标还是键盘切换都会触发）
2、currentRowChanged -- 所选的行改变时会触发（无论使用鼠标还是键盘切换都会触发）
3、currentTextChanged -- 当前项目文本改变时会触发
4、itemClicked -- 鼠标单击或双击项目时都会触发
5、itemDoubleClicked -- 鼠标双击项目时会触发
6、itemSelectionChanged -- 项目切换就会触发
"""
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class list_widget(QListWidget):
    def __init__(self):
        super(list_widget, self).__init__()
        item = QListWidgetItem(QIcon('./img/xing.png'), '1. Python')
        self.addItem(item)
        self.addItem(QListWidgetItem(QIcon('./img/xing.png'), '2. Java'))
        self.addItem(QListWidgetItem(QIcon('./img/xing.png'), '3. C/C++'))

        # print(self.indexFromItem(item).data())


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.window_ui()

    def window_ui(self):
        lw = list_widget()
        button = QPushButton('Test')
        box = QVBoxLayout()
        box.addWidget(lw)
        box.addWidget(button)
        self.setLayout(box)

        def window_event():
            # print(lw.item(0).text())
            # print(lw.takeItem(0))
            lw.setCurrentRow(2)

        def do_something():
            print('hello')

        button.clicked.connect(window_event)
        lw.itemSelectionChanged.connect(do_something)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
