# QTableWidget -- 表格控件
"""
QTableWidget常用api：
1、column()、row() -- 返回项目所在的行和列
2、columnCount()、rowCount() -- 返回列数和行数
3、currentColumn()、currentRow() -- 返回所在的列和行
4、currentItem() -- 返回当前选择的项目
5、indexFromItem() -- 返回指定项目的QModelIndex
6、itemFromIndex() -- 返回指定QModelIndex的项目
7、item() -- 返回指定单元格中的项目
8、selectedItems() -- 返回由选定项目组成的列表，如果没有选中项目，则返回空列表
9、setCurrentCell() -- 设置当前选定的项目
10、setCurrentItem() -- 设置当前选定的项目
11、setHorizontalHeaderItem()、setHorizontalHeaderLabels()、setVerticalHeaderItem()、setVerticalHeaderLabels() -- 设置水平标题和垂直标题
12、setItem() -- 添加项目
13、takeItem() -- 删除项目
14、insertColumn()、insertRow() -- 插入空列和空行
15、clear() -- 清空所有数据，包括标题
16、clearContents() -- 清空所有数据，不包括标题
17、removeColumn()、removeRow() -- 删除行和列


QTableWidget常用信号：
1、cellChanged -- 当单元格发生改变时会触发
2、itemChanged -- 当项目发生改变时会触发
3、cellClicked -- 点击单元格就会触发
4、itemClicked -- 点击项目时会触发，如果单元格中没有项目不会触发
5、cellDoubleClicked -- 双击单元格就会触发
6、itemDoubleClicked -- 双击项目时会触发，如果单元格中没有项目不会触发
7、currentCellChanged -- 当前所选择的单元格发生改变就会触发此信号（无论是使用鼠标单击还是键盘按键切换单元格，或是双击单元格之后进行修改拟或不修改）
8、currentItemChanged -- 使用鼠标单击或者键盘按钮切换到包含项目的单元格时，或者切换离开包含项目的单元格时，双击包含项目的单元格之后进行修改拟或不修改时，会触发此信号
"""
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class table_widget(QTableWidget):
    def __init__(self, row, column):
        super(table_widget, self).__init__(row, column)
        self.table_item = QTableWidgetItem('30')
        self.setItem(0, 0, QTableWidgetItem('zhangsan'))
        self.setItem(0, 1, self.table_item)
        self.setItem(1, 0, QTableWidgetItem('laowang'))
        self.setItem(1, 1, QTableWidgetItem('46'))
        self.insertRow(1)
        self.setHorizontalHeaderLabels(['name', 'age'])
        # self.clear()
        # self.clearContents()
        # print(self.row(self.table_item))


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.window_ui()

    def window_ui(self):
        tw = table_widget(2, 2)
        button = QPushButton('Test')
        box = QVBoxLayout()
        box.addWidget(tw)
        box.addWidget(button)
        self.setLayout(box)

        def window_event():
            # print(tw.item(0, 0).text())
            # print(tw.selectedItems())
            # tw.setCurrentItem(tw.table_item)
            # tw.setCurrentCell(0, 1)
            # tw.setItem(0, 0, QTableWidgetItem('lisi'))
            # print(tw.currentIndex())
            # print(tw.column(tw.table_item))
            # print(tw.row(tw.table_item))
            # print(tw.currentItem())
            # print(tw.selectedItems())
            tw.takeItem(0, 0)

        button.clicked.connect(window_event)
        # tw.cellClicked.connect(self.window_event)

    def window_event(self):
        print('hello world')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
