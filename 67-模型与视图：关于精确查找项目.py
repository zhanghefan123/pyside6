# 在QListWidget、QTableWidget、QTreeWidget中如何精确的找到项目？
# finditems()
"""
可使用的MatchFlag枚举值：

    Qt.MatchExactly -- 搜索大小写和长度都必须完全符合text的项目；注：可用于图标视图中查找图标的文件名
    Qt.MatchContains -- 搜索所有包含text的项目，搜索时忽略大小写
    Qt.MatchStartsWith -- 搜索所有以text开始的项目，搜索时忽略大小写
    Qt.MatchEndsWith -- 搜索所有以text结尾的项目，搜索时忽略大小写
    Qt.MatchRegularExpression -- 以正则表达式的text来进行匹配搜索
    Qt.MatchWildcard -- 允许text中包含通配符来进行匹配搜索，搜索时忽略大小写；注：*表示0~无限个字符，?表示单个字符
    Qt.MatchFixedString -- 执行基于字符串的匹配搜索，搜索时忽略大小写
    Qt.MatchCaseSensitive -- 执行基于字符串的匹配搜索，搜索时区分大小写
    Qt.MatchWrap -- 执行环绕式搜索，以便当搜索到达模型中的最后一个项目时，它从第一个项目再次开始，并持续到所有项目都经过检查
    Qt.MatchRecursive -- 可搜索多层次项目，如果项目没有子项，则只匹配顶层

    注：也适用于QAbstractItemModel类的match方法
"""
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class table_widget(QTableWidget):
    def __init__(self, row, column):
        super(table_widget, self).__init__(row, column)
        self.setItem(0, 0, QTableWidgetItem('zhangsan'))
        self.setItem(0, 1, QTableWidgetItem('30'))
        self.setItem(0, 2, QTableWidgetItem('软件工程师'))
        self.setItem(1, 0, QTableWidgetItem('laowang'))
        self.setItem(1, 1, QTableWidgetItem('46'))
        self.setItem(1, 2, QTableWidgetItem('全栈工程师'))
        self.setItem(2, 0, QTableWidgetItem('lisi'))
        self.setItem(2, 1, QTableWidgetItem('35'))
        self.setItem(2, 2, QTableWidgetItem('架构师'))
        self.setHorizontalHeaderLabels(['name', 'age', 'job'])


class tree_widget(QTreeWidget):
    def __init__(self):
        super(tree_widget, self).__init__()
        self.setHeaderLabels(['目录', '详细信息'])
        self.item1 = QTreeWidgetItem(['图片', '存放各种图片...'])
        item2 = QTreeWidgetItem(['progress', '存放项目...'])
        item3 = QTreeWidgetItem(['资料', '存放各种资料'])
        item1_c1 = QTreeWidgetItem(['xing.png'])
        item1_c2 = QTreeWidgetItem(['file.png'])
        self.addTopLevelItem(self.item1)
        self.addTopLevelItems([item2, item3])
        self.item1.addChildren([item1_c1, item1_c2])


class Model(QStandardItemModel):
    def __init__(self):
        super(Model, self).__init__()
        for i in range(10):
            self.appendRow(QStandardItem('Python'))


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.window_ui()

    def window_ui(self):
        # tw = table_widget(3, 3)
        # tw = tree_widget()
        _view = QListView()
        _model = Model()
        _view.setModel(_model)
        button = QPushButton('Test')
        box = QVBoxLayout()
        # box.addWidget(tw)
        box.addWidget(_view)
        box.addWidget(button)
        self.setLayout(box)

        def window_event():
            # find_item = tw.findItems('*.png', Qt.MatchRecursive | Qt.MatchWildcard)
            # find_item = tw.findItems('zhangsan', Qt.MatchFixedString)
            # print(find_item[1].text(0))

            find_item = _model.match(_model.index(4, 0), Qt.DisplayRole, 'Python', -1, Qt.MatchExactly)
            for i in find_item:
                print(f'{find_item.index(i) + 1} {i.data()}')

        button.clicked.connect(window_event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
