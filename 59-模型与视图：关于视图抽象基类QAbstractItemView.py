# QAbstractItemView -- 标准视图抽象基类，本身无法实例化
# 官方文档：它提供了一个标准界面，通过信号和插槽机制与模型互操作，使子类能够随时了解模型的变化；该类对键盘和鼠标的导航、视窗的滚动、项的编辑以及选择提供了标准的支持
"""
QAbstractItemView常用api：
1、setSelectionMode() -- 设置视图如何响应用户选择，有如下枚举值可用：

    QAbstractItemView.SingleSelection：当用户选择一个项目时，任何已经选择的项目都会被取消选择；用户可以在单击所选项目时按下Ctrl键来取消选择所选项目
    QAbstractItemView.ContiguousSelection：当用户以通常的方式选择项目时，将清除所选项目并选择新项目；但是，如果用户在单击项目时按下Shift键，则根据单击项目的状态，选择或取消选择当前项目和单击的项目之间的所有项目
    QAbstractItemView.ExtendedSelection：当用户以通常的方式选择项目时，将清除所选项目并选择新项目；但是，如果用户在单击项目时按下Ctrl键，则单击的项目将被切换，所有其他项目保持不变。如果用户在单击项目时按下Shift键，则根据单击项目的状态，选择或取消选择当前项目和单击的项目之间的所有项目。通过将鼠标拖过多个项目，可以选择它们。
    QAbstractItemView.MultiSelection：当用户以通常的方式选择项目时，将切换该项目的选择状态，并将其他项目单独留下；可以通过将鼠标拖动到多个项目上来切换它们。
    QAbstractItemView.NoSelection：无法选择项目

2、setSelectionBehavior() -- 设置选择行为，有三个值可用：
    QAbstractItemView.SelectItems：选择单个项目
    QAbstractItemView.SelectRows：仅选择行
    QAbstractItemView.SelectColumns：仅选择列

3、setEditTrigger() -- 设置项的编辑方式

    QAbstractItemView.NoEditTriggers：无法编辑
    QAbstractItemView.CurrentChanged：每当当前项目发生变化时，编辑就开始了
    QAbstractItemView.DoubleClicked：当一个项目被双击时，编辑就开始了
    QAbstractItemView.SelectedClicked：单击已选择的项目时开始编辑
    QAbstractItemView.EditKeyPressed：当平台编辑键被按在项目上时，编辑就开始了
    QAbstractItemView.AnyKeyPressed：当任何键按在项目上时，编辑就开始了
    QAbstractItemView.AllEditTriggers：开始编辑上述所有操作

4、currentIndex() -- 返回当前项目的QModelIndex
5、setTabKeyNavigation() -- 是否支持tab键和(shift+tab)的导航
6、setTextElideMode() -- 省略号在文本中出现的位置，默认值在右侧，有四个值可用：Qt.ElideLeft、Qt.ElideMiddle、Qt.ElideRight、Qt.ElideNone
7、setIconSize() -- 设置图标尺寸
8、setAutoScroll() -- 设置是否开启自动滚动：如果用户在视图边缘的16像素内拖动，QAbstractItemView会自动滚动视图的内容、如果当前项发生变化，则视图将自动滚动以确保当前项完全可见（默认开启）
9、setAutoScrollMargin() -- 设置自动滚动触发的范围，单位是像素，默认是16像素
10、setVerticalScrollMode() -- 设置垂直滚动模式
11、setHorizontalScrollMode() -- 设置水平滚动模式
    QAbstractItemView.ScrollPerItem：一次滚动一个项目的内容
    QAbstractItemView.ScrollPerPixel：一次滚动一个像素的内容

12、clearSelection() -- 取消所有选定
13、scrollToBottom() -- 滚动到视图底部
14、scrollToTop() -- 滚动到视图顶部
15、selectAll() -- 全选所有项目

16、setItemDelegate() -- 为视图设置"委托"
17、setItemDelegateForColumn() -- 为指定的列设置"委托"
18、setItemDelegateForRow() -- 为指定的行设置"委托"
19、itemDelegate()、itemDelegateForColumn()、itemDelegateForRow() -- 返回"委托"对象


QAbstractItemView常用信号：
1、activated -- 当"激活"项目时会触发（注：在macOS中无反应）
2、clicked -- 点击并释放了项目就会触发（双击也会触发）
3、doubleClicked -- 双击了项目时会触发
4、entered -- 鼠标光标进入项目范围时会触发（注：需要开启鼠标跟踪：setMouseTracking()）
5、iconSizeChanged -- 项目图标尺寸发生改变时会触发
6、pressed -- 按下鼠标按钮就会触发
7、viewportEntered -- 鼠标光标进入视图范围就会触发（注：需要开启鼠标跟踪：setMouseTracking()）
"""

import sys, time
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class list_view(QListView):
    def __init__(self):
        super(list_view, self).__init__()
        # self.setMouseTracking(True)


class table_view(QTableView):
    def __init__(self):
        super(table_view, self).__init__()
        # self.setSelectionMode(QAbstractItemView.SingleSelection)
        # self.setSelectionBehavior(QAbstractItemView.SelectColumns)


class list_model(QStandardItemModel):
    def __init__(self):
        super(list_model, self).__init__()
        self.appendRow(QStandardItem(QIcon('./img/xing.png'), '1. Python'))
        self.appendRow(QStandardItem(QIcon('./img/xing.png'), '2. Java'))
        self.appendRow(QStandardItem(QIcon('./img/xing.png'), '3. Go'))
        self.appendRow(QStandardItem(QIcon('./img/xing.png'), '4. C/C++'))
        self.appendRow(QStandardItem(QIcon('./img/xing.png'), '5. C#'))
        self.appendRow(QStandardItem(QIcon('./img/xing.png'), '6. JavaScript'))


class table_model(QStandardItemModel):
    def __init__(self):
        super(table_model, self).__init__()
        self.insertRow(0, [QStandardItem('Python'), QStandardItem('Java')])
        self.insertRow(1, [QStandardItem('C/C++'), QStandardItem('Go')])


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.window_ui()

    def window_ui(self):
        model = list_model()
        # model = table_model()
        view = list_view()
        # view = table_view()
        view.setModel(model)
        button = QPushButton('Test')
        box = QGridLayout()
        box.addWidget(view, 0, 0, 3, 1)
        box.addWidget(button, 3, 0, 1, 1)
        self.setLayout(box)
        # self.setFixedWidth(100)
        def window_event():
            view.scrollToBottom()

        def do_something():
            print('hello world')

        button.clicked.connect(window_event)
        view.activated.connect(do_something)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
