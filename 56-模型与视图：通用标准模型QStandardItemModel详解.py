# QStandardItemModel -- 通用标准模型类，实现了QAbstractItemModel接口，
# 该模型可以为任何支持该接口的视图提供数据（可以实现全部三种数据组织结构）
# 列表，表格以及树形结构都可以使用他进行实现
# QStandardItemModel使用QStandardItem作为数据支撑，即由我们的QStandardItem来组成
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


# 列表视图的呈现方式
class list_model(QStandardItemModel):
    def __init__(self):
        super(list_model, self).__init__()
        # self.setRowCount(3)
        item1 = QStandardItem('Java')
        self.appendRow(QStandardItem('Python'))
        self.appendRow(item1)
        self.appendRow(QStandardItem('C/C++'))
        # 我们还可以传递一个列表-但是在实际的情况下只能第一个生效
        self.appendRow([QStandardItem('C#'), QStandardItem('PHP')])
        # 行索引从1开始
        self.insertRow(1, QStandardItem('ruby'))
        # self.setItem(0, QStandardItem('ruby'))
        # print(self.indexFromItem(item1))
        # self.setData(self.index(0, 0), 'ruby', Qt.DisplayRole)
        # Qt.DisplayRole就是显示我们的数据
        print(self.data(self.index(1, 0), Qt.DisplayRole))
        # 下面进行重新的某一项的设置
        self.setData(self.index(0, 0), "zhf")


# 表格视图的呈现方式
class table_model(QStandardItemModel):
    def __init__(self):
        super(table_model, self).__init__()
        self.insertRow(0, [QStandardItem('Python'), QStandardItem('Java')])
        self.insertRow(1, [QStandardItem('C/C++'), QStandardItem('Go')])
        # 注意行列可以是不完全一致的
        self.insertColumn(0, [QStandardItem('C#'), QStandardItem('PHP'), QStandardItem('Ruby')])
        # 返回第二行第二列的值
        print(self.item(1, 1).text())

        # 这样会限制总共只存在两行两列的数据，其他的数据都将被截断
        # self.setRowCount(2)
        # self.setColumnCount(2)
        # 并且如果一开始就进行设置，那么我们需要将其放到前面。

        # setItem()方法，我们传递的是行索引，和列索引，以及设置的项目
        self.setItem(0, 0, QStandardItem('Ruby'))

        # 下面进行的是水平标题的设置
        self.setHorizontalHeaderLabels(['name', 'age', "year"])
        # 下面进行的是垂直的标题的设置
        self.setVerticalHeaderLabels(['name', 'age', "year"])


# 树视图的呈现方式
class tree_model(QStandardItemModel):
    def __init__(self):
        super(tree_model, self).__init__()
        self.c_c = QStandardItem('C/C++')
        self.appendRow(QStandardItem('Python'))
        self.appendRow(QStandardItem('Java'))
        self.appendRow(self.c_c)
        # 为我们的c_c结点进行子结点的设置
        # 第一个子结点位于第0行第0列
        # 第二个子结点位于第1行第0列
        self.c_sharp = QStandardItem('C#')
        self.c_c.setChild(0, 0, QStandardItem('C++'))
        self.c_c.setChild(1, 0, QStandardItem('C'))
        self.c_c.setChild(2, 0, self.c_sharp)

        self.c_sharp.setChild(0, 0, QStandardItem('C#1'))

        # 然后我们可以通过index进行指定项目所处的行，列，父级


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.window_ui()

    def window_ui(self):
        model = list_model()
        # model = table_model()
        # model = tree_model()
        # 找到第0行，第0列然后进行取值的操作
        print(model.index(0, 0).data())
        # model.indexFromItem(item) 用来传递一个item获得一个index
        # model.itemFromIndex(index) 用来传递一个index获得一个item
        view = QListView()
        # view = QTableView()
        # view = QTreeView()
        view.setModel(model)
        # 我们的view可以将数据存放进去
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
