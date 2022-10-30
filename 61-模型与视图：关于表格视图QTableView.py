# QTableView -- 表格视图
"""
QTableView常用api：
1、setRowHeight() -- 设置行高（注意：此方法要置于setModel之后才会有效果）
2、setColumnWidth() -- 设置列宽（注意：此方法要置于setModel之后才会有效果）
3、setSpan() -- 设置行或列的跨度
4、clearSpans() -- 清除所有的跨度
5、horizontalHeader()、verticalHeader() -- 返回水平头部和垂直头部
6、setCornerButtonEnabled() -- 设置左上角的全选按钮是否可用
7、setWordWrap() -- 设置文本自动换行（即使开启了自动换行，单元格将不会为了适应全部长度的文本而扩大，而是根据textElideMode策略在文本中添加省略号）
8、setSortingEnabled() -- 设置是否开启排序
9、sortByColumn() -- 如果开启排序，会以此方法定的规则来进行排序；可以使用两个枚举值：Qt.AscendingOrder（升序）、Qt.DescendingOrder（降序）
10、setShowGrid() -- 设置是否显示网格，默认开启
11、hideColumn()、hideRow() -- 隐藏指定的行和列
12、showColumn()、showRow() -- 显示指定的行和列
13、resizeColumnToContents() -- 根据用于呈现列中每个项目的代理的大小提示调整给定列的大小（自动调节列宽）
14、resizeRowToContents() -- 根据用于呈现列中每个项目的代理的大小提示调整给定行的大小（自动调节行高）
15、selectColumn() -- 选定指定的列
16、selectRow() -- 选定指定的行
17、setHorizontalHeader() -- 设置水平标题
18、setVerticalHeader() -- 设置垂直标题
"""
import sys, time
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class view(QTableView):
    def __init__(self):
        super(view, self).__init__()
        # self.setRowHeight(1, 200)
        # self.setColumnWidth(0, 300)
        # self.setIndexWidget(self.model().index(0, 0), QPushButton('test'))
        # self.setSpan(0, 0, 1, 2)
        header = self.horizontalHeader()
        # print(header)
        # self.resizeRowToContents(0)
        # self.setWordWrap(True)
        # self.setCornerButtonEnabled(False)



class model_(QStandardItemModel):
    def __init__(self):
        super(model_, self).__init__()
        self.appendRow([QStandardItem('zhangsanzhangsanzhangsanzhangsanzhangsan'), QStandardItem('30'),
                        QStandardItem('软件工程师')])
        self.appendRow([QStandardItem('lisi'), QStandardItem('22'), QStandardItem('测试工程师')])
        self.appendRow([QStandardItem('laowang'), QStandardItem('46'), QStandardItem('网络架构师')])
        self.appendRow([QStandardItem('xiaoming'), QStandardItem('34'), QStandardItem('全栈架构师')])


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.window_ui()

    def window_ui(self):
        _view = view()
        _model = model_()
        _view.setModel(_model)
        # _view.setRowHeight(0, 100)
        # _view.setColumnWidth(0, 100)
        # _view.sortByColumn(1, Qt.DescendingOrder)
        _view.resizeColumnsToContents()
        button = QPushButton('Test')
        box = QVBoxLayout()
        box.addWidget(_view)
        box.addWidget(button)
        self.setLayout(box)

        def window_event():
            _view.clearSpans()

        button.clicked.connect(window_event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
