# QModelIndex -- 模型索引；模型、视图都依靠索引定位到数据
"""
QModelIndex常用api：
1、column() -- 返回索引所在的列
2、row() -- 返回索引所在的行
3、model() -- 返回索引所在的模型
4、data() -- 根据数据"角色"返回数据内容
5、sibling() -- 返回同级的兄弟
6、siblingAtColumn() -- 返回同级的列的兄弟
7、siblingAtRow() -- 返回同级的行的兄弟

注：sibling、siblingAtColumn、siblingAtRow虽然可用于全部三种数据组织形式中，但是在树结构中较为实用
"""
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class table_view(QTableView):
    def __init__(self):
        super(table_view, self).__init__()


class tree_view(QTreeView):
    def __init__(self):
        super(tree_view, self).__init__()


class table_model(QStandardItemModel):
    def __init__(self):
        super(table_model, self).__init__()
        self.setHorizontalHeaderLabels(['物品', '单价', '数量'])
        self.appendRow([QStandardItem('iPhone X'), QStandardItem('8000'), QStandardItem('10')])
        self.appendRow([QStandardItem('iPhone 6'), QStandardItem('3000'), QStandardItem('0')])
        self.appendRow([QStandardItem('MacBook Air'), QStandardItem('10000'), QStandardItem('0')])

        # print(self.index(1, 1).sibling(0, 0))


class tree_model(QStandardItemModel):
    def __init__(self):
        super(tree_model, self).__init__()
        self.setHorizontalHeaderLabels(['项目'])
        self.appendRow(QStandardItem(QIcon('./photo/call.png'), 'Python'))
        self.appendRow(QStandardItem(QIcon('./photo/call.png'), 'Java'))
        self.appendRow(QStandardItem(QIcon('./photo/call.png'), '和C相关'))
        c_index = self.index(2, 0)
        c_item = self.itemFromIndex(c_index)
        c_item.setChild(0, 0, QStandardItem('C'))
        c_item.setChild(1, 0, QStandardItem('C++'))
        c_item.setChild(2, 0, QStandardItem('C#'))


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.window_ui()

    def window_ui(self):
        # _model = table_model()
        _model = tree_model()
        # _view = table_view()
        _view = tree_view()
        _view.setModel(_model)
        button = QPushButton('Test')
        box = QVBoxLayout()
        box.addWidget(_view)
        box.addWidget(button)
        self.setLayout(box)

        def window_event():
            pass
            # print(_model.index(0, 0, _model.index(2, 0)).data())
            # c = _model.index(0, 0, _model.index(2, 0))

        button.clicked.connect(window_event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
