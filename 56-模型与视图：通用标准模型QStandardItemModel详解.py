# QStandardItemModel -- 通用标准模型类，实现了QAbstractItemModel接口，该模型可以为任何支持该接口的视图提供数据（可以实现全部三种数据组织结构）
# QStandardItemModel使用QStandardItem作为数据支撑
"""
QStandardItemModel常用api：
1、appendRow()、insertRow() -- 添加行的项目；（注意：适用于列表、表格和树）
2、appendColumn()、insertColumn() -- 添加列的项目；（注意：适用于表格和树；insertColumn也可用于列表）
3、setRowCount() -- 设置行数；（注意：适用于列表、表格和树，如果先指定了行数，添加项目时需使用insert开头的方法）
4、setColumnCount() -- 设置列数；（注意：适用于表格和树）
5、setItem() -- 将项目放入模型；（注意：适用于列表、表格和树）
6、invisibleRootItem() -- 返回根节点，类型是QStandardItem
7、findItems() -- 查找项目，返回的类型是QStandardItem
8、index() -- 通过指定项目的行、列、父级返回对应的QModelIndex
9、indexFromItem() -- 通过item返回对应的QModelIndex
10、setVerticalHeaderItem()、setVerticalHeaderLabels()、setHorizontalHeaderLabels()、setHorizontalHeaderItem() -- 设置水平标题和垂直标题；（注意：适用于表格；其中设置水平标题也适用于树）
11、item() -- 返回指定位置的项目，类型是QStandardItem；（注意：适用于列表、表格和树）
12、itemFromIndex() -- 通过QModelIndex返回对应的item
13、takeRow() -- 删除行；（注意：适用于列表、表格和树）
14、takeColumn() -- 删除列；（注意：适用于表格和树）
15、takeItem() -- 删除项目，但不删除行和列，返回值是被删除的项目，类型是QStandardItem；（注意：适用于列表、表格和树）
16、clear() -- 删除所有项目，包括标题项目，并将行和列设置为0
17、setData() -- 修改现有QModelIndex处的数据
18、data() -- 返回指定QModelIndex处的数据
"""
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class list_model(QStandardItemModel):
    def __init__(self):
        super(list_model, self).__init__()
        # self.setRowCount(3)
        item1 = QStandardItem('Java')
        self.appendRow(QStandardItem('Python'))
        self.appendRow(item1)
        self.appendRow(QStandardItem('C/C++'))
        # self.insertRow(1, QStandardItem('ruby'))
        # self.setItem(0, QStandardItem('ruby'))
        # print(self.indexFromItem(item1))
        # self.setData(self.index(0, 0), 'ruby', Qt.DisplayRole)
        print(self.data(self.index(1, 0), Qt.FontRole))


class table_model(QStandardItemModel):
    def __init__(self):
        super(table_model, self).__init__()
        self.insertRow(0, [QStandardItem('Python'), QStandardItem('Java')])
        self.insertRow(1, [QStandardItem('C/C++'), QStandardItem('Go')])
        # print(self.item(1, 1).text())
        # self.setRowCount(2)
        # self.setColumnCount(2)
        # self.setHorizontalHeaderLabels(['name', 'age'])
        # self.setVerticalHeaderItem(0, QStandardItem('name'))
        # self.setVerticalHeaderItem(1, QStandardItem('age'))
        # self.setVerticalHeaderLabels(['name', 'age'])


class tree_model(QStandardItemModel):
    def __init__(self):
        super(tree_model, self).__init__()
        self.c_c = QStandardItem('C/C++')
        self.appendRow(QStandardItem('Python'))
        self.appendRow(QStandardItem('Java'))
        self.appendRow(self.c_c)
        # self.c_c.setChild(0, 0, QStandardItem('C++'))
        # self.c_c.setChild(1, 0, QStandardItem('C'))


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.window_ui()

    def window_ui(self):
        model = list_model()
        # model = table_model()
        # model = tree_model()
        view = QListView()
        # view = QTableView()
        # view = QTreeView()
        view.setModel(model)
        button = QPushButton('Test')
        box = QVBoxLayout()
        box.addWidget(view)
        box.addWidget(button)
        self.setLayout(box)

        def window_event():
            # print(model.itemFromIndex(model.index(0, 0, model.c_c.index())).text())
            print(model.takeItem(1))
            # print(model.findItems('Java'))
            # print(model.index(0, 0).data())
            # print(model.i)

        button.clicked.connect(window_event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
