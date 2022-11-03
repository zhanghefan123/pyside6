# QTreeView -- 树视图
"""
QTreeView常用api：
1、collapse()、collapseAll() -- 折叠项目
2、expand()、expandAll() -- 展开项目
3、expandRecursively() -- 通过QModelIndex展开项目到指定的层级(depth，-1表示展开此项下的所有层级)
4、header() -- 返回视图的标题对象
5、setItemsExpandable() -- 设置项目是否可以展开
6、resizeColumnToContents() -- 按项目内容调整"最合适列宽"
7、setRowHidden() -- 隐藏行
8、setColumnHidden() -- 隐藏列
9、setAnimated() -- 使项目展开时带有动态效果
10、setColumnWidth() -- 设置列宽
11、setHeader() -- 设置视图标题
12、setHeaderHidden() -- 隐藏标题
13、setIndentation() -- 设置项目缩进值
14、setSortingEnabled() -- 设置是否开启排序
15、sortByColumn() -- 如果开启排序，则调用此方法中的排序规则
16、setWordWrap() -- 设置自动换行
"""
import sys, time
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class view(QTreeView):
    def __init__(self):
        super(view, self).__init__()
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.setItemsExpandable(False)
        self.setAnimated(True)
        # self.setIndentation(15)
        self.resizeColumnToContents(0)


class model(QStandardItemModel):
    def __init__(self):
        super(model, self).__init__()
        self.appendRow(QStandardItem(QIcon('icons/file_open.png'), 'test'))
        self.appendRow(QStandardItem(QIcon('icons/file_open.png'), 'HBuilderProjects'))
        self.appendRow(QStandardItem(QIcon('icons/file_open.png'), '文件夹'))
        self.itemFromIndex(self.index(1, 0)).appendRow(QStandardItem(QIcon('icons/file.png'), 'test1.py'))
        self.itemFromIndex(self.index(1, 0)).appendRow(QStandardItem(QIcon('icons/file.png'), 'new.html'))
        item1 = self.itemFromIndex(self.index(0, 0))
        item1.appendRow(QStandardItem(QIcon('icons/file_open.png'), '图片'))
        item1.appendRow(QStandardItem(QIcon('icons/file_open.png'), '下载'))
        self.itemFromIndex(self.index(0, 0, self.indexFromItem(item1))).appendRow(QStandardItem('go.png'))
        self.setHorizontalHeaderLabels(['目录', '尺寸', '修改日期', '详细信息'])


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.window_ui()

    def window_ui(self):
        _model = model()
        _view = view()
        _view.setModel(_model)
        button = QPushButton('Test')
        box = QGridLayout()
        box.addWidget(_view, 0, 0, 3, 1)
        box.addWidget(button, 3, 0, 1, 1)
        self.setLayout(box)

        # self.setFixedWidth(100)
        def window_event():
            # _view.collapse(_model.index(0, 0))
            # _view.expandRecursively(_model.index(0, 0), 0)
            _view.setRowHidden(1, QModelIndex(), True)

        button.clicked.connect(window_event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
