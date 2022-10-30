# QStandardItem -- 模型项
"""
QStandardItem常用api：
1、index() -- 返回项的QModelIndex
2、setChild() -- 设置子项
3、setBackground() -- 设置项的背景
4、setCheckable() -- 设置项是否可勾选
5、setCheckState() -- 设置勾选的状态；有三个值：Qt.PartiallyChecked、Qt.Unchecked、Qt.Checked
6、setEditable() -- 设置项可编辑
7、setEnabled() -- 设置项可用
8、setFont() -- 设置项的字体
9、setIcon() -- 设置项的图标
10、setSelectable() -- 设置项是否可选择
11、setTextAlignment() -- 设置项的对齐方式
12、setUserTristate() -- 设置项可使用三种勾选状态
13、parent() -- 返回项的父级，类型是QStandardItem
14、setData() -- 设置项的数据

15、appendRow() -- 添加项的行子项，insertRow()用法相同；（注意：适用于树）
16、appendColumn() -- 添加项的列子项，insertColumn()用法相同；（注意：适用于树）
17、takeRow() -- 删除指定的子项的行；注意：删除某子项行后，后面的子项行会补位
18、takeColumn() -- 删除指定的子项的列；注意：删除某子项列后，后面的子项列会补位
19、takeChild() -- 删除指定位置的子项
"""
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class list_model(QStandardItemModel):
    def __init__(self):
        super(list_model, self).__init__()
        item = QStandardItem('Java')
        self.appendRow(QStandardItem('Python'))
        self.appendRow(item)
        self.appendRow(QStandardItem('C/C++'))

        print(item.index().data())


class table_model(QStandardItemModel):
    def __init__(self):
        super(table_model, self).__init__()
        self.insertRow(0, [QStandardItem('Python'), QStandardItem('Java')])
        self.insertRow(1, [QStandardItem('C/C++'), QStandardItem('Go')])
        item = QStandardItem('hello world')
        # item.setBackground(QColor('red'))
        # item.setSelectable(False)
        # item.setCheckable(True)
        # item.setUserTristate(True)
        # item.setCheckState(Qt.PartiallyChecked)
        # item.setToolTip('hello world')
        self.appendRow(item)


class Item(QStandardItem):
    def __init__(self, text):
        super(Item, self).__init__(text)
        # self.setCheckable(True)


class tree_model(QStandardItemModel):
    def __init__(self):
        super(tree_model, self).__init__()
        self.setHorizontalHeaderLabels(['目录', '详细信息', '大小'])
        self.appendRow(QStandardItem(QIcon('./photo/file_open.png'), 'data'))
        self.appendRow(QStandardItem(QIcon('./photo/file_open.png'), 'Adobe'))
        test = QStandardItem(QIcon('./photo/file_open.png'), 'test')
        self.appendRow(test)

        test.appendRow(QStandardItem(QIcon('./photo/file.png'), 'test1.py'))
        test.appendRow(QStandardItem(QIcon('./photo/file.png'), 'test2.py'))
        test.appendRow(QStandardItem(QIcon('./photo/file.png'), 'test3.py'))
        test.appendColumn(
            [QStandardItem('this is test1'), QStandardItem('this is test1'), QStandardItem('this is test1')])
        test.appendColumn([QStandardItem('234K'), QStandardItem('1.3G')])

        # test.takeChild(0, 1)
        test.takeRow(1)


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.window_ui()

    def window_ui(self):
        # model = list_model()
        # model = table_model()
        model = tree_model()
        # view = QListView()
        # view = QTableView()
        view = QTreeView()
        view.setModel(model)
        button = QPushButton('Test')
        box = QVBoxLayout()
        box.addWidget(view)
        box.addWidget(button)
        self.setLayout(box)
        self.setFixedWidth(500)

        def window_event():
            pass

        button.clicked.connect(window_event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
