# QTreeWidget -- 树控件
"""
QTreeWidget常用api：
1、addTopLevelItem()、addTopLevelItems() -- 添加项目
2、currentItem() -- 返回当前选择的项目
3、indexFromItem() -- 返回指定项目的QModelIndex
4、itemFromIndex() -- 返回指定QModelIndex的项目
5、insertTopLevelItem()、insertTopLevelItems() -- 在指定位置插入项目
6、invisibleRootItem() -- 返回根节点
7、itemAbove() -- 返回当前选择的项目上方的项目
8、itemBelow() -- 返回当前选择的项目下方的项目
9、setColumnCount() -- 设置列数
10、setCurrentItem() -- 设置当前选择的项目
11、setHeaderItem()、setHeaderLabel() -- 设置标题项目或标签文本
12、setHeaderLabels() -- 设置多列的标题标签文本
13、sortItems() -- 设置排序；排序方式有两个值可用：Qt.AscendingOrder（升序）、Qt.DescendingOrder（降序）
14、takeTopLevelItem() -- 删除项目
15、topLevelItem() -- 返回指定的项目
16、topLevelItemCount() -- 返回控件中的项目数量
17、collapseItem() -- 折叠项目
18、expandItem() -- 展开项目


QTreeWidget常用信号：
1、currentItemChanged -- 当前选择的项目发生改变时就会触发（无论使用鼠标点击、双击或是键盘按键切换项目时均会触发）
2、itemCollapsed -- 项目折叠时会触发
3、itemExpanded -- 项目展开时会触发
4、itemClicked -- 点击项目时会触发
5、itemDoubleClicked -- 双击项目时会触发
6、itemEntered -- 单击项目时触发（多次单击时并不会触发）
"""
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


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
        # self.setColumnCount(1)


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.window_ui()

    def window_ui(self):
        tw = tree_widget()
        button = QPushButton('Test')
        box = QVBoxLayout()
        box.addWidget(tw)
        box.addWidget(button)
        self.setLayout(box)

        def window_event():
            # print('hello world')
            # print(tw.itemAbove(tw.currentItem()).text(0))
            # tw.setCurrentItem(tw.item1)
            # tw.sortItems(0, Qt.AscendingOrder)
            # tw.takeTopLevelItem(0)
            # print(tw.topLevelItemCount())
            # tw.collapseItem(tw.item1)
            tw.expandItem(tw.item1)
            # print(tw.currentItem().text(1))
            # print(tw.topLevelItem(0).text(0))

        button.clicked.connect(window_event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
