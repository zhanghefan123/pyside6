# QModelIndex -- 模型索引；模型、视图都依靠索引定位到数据
"""
QModelIndex常用api：
1、column() -- 返回索引所在的列
2、row() -- 返回索引所在的行
3、model() -- 返回索引所在的模型
4、data() -- 根据数据"角色"返回数据内容

列表和表格之中没有同级的概念，所以只需要通过行来进行定位，而树型模型之中有同级的概念，所以需要通过行、列、父级来进行定位
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
        self.appendRow(QStandardItem(QIcon('icons/call.png'), 'Python'))
        self.appendRow(QStandardItem(QIcon('icons/call.png'), 'Java'))
        self.appendRow(QStandardItem(QIcon('icons/call.png'), '和C相关'))
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
            # 默认第一级是不需要进行父的指定的，因为他默认就是根结点
            # 下面的代码之中的_model.index(2,0)找到的就是我们的顶层第三项和c相关
            print(_model.index(0, 0, _model.index(2, 0)).data())
            c = _model.index(0, 0, _model.index(2, 0))
            # 拿到同一级的，就可以很方便地进行同级的兄弟获取
            print(c.sibling(1, 0))

        button.clicked.connect(window_event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
