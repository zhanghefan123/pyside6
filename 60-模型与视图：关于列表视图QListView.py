# QListView -- 列表视图
"""
QListView常用api：
1、setFlow() -- 设置项的排列方向，有两个值可用：QListView.LeftToRight（左到右）、QListView.TopToBottom（上到下）
2、setLayoutMode() -- 设置布局模式，有两个值可用：QListView.SinglePass（一次性列出）、QListView.Batched（分批列出）
3、setViewMode() -- 设置视图模式，有两个值可用：
    QListView.ListMode：视图中的项目以列表的形式从上到下排列
    QListView.IconMode：视图中的项目以图标的形式从左到右排列

4、setBatchSize() -- 布局模式为Batched是前提；设置每批显示的项目数
5、setWrapping() -- 设置自动换行
6、setItemAlignment() -- 设置项目在视图中的对齐方式
7、setResizeMode() -- 设置重新布局模式，当视图大小改变时是否重新布局，有两个值可用：QListView.Fixed（只在一开始布局一次）、QListView.Adjust（随时重新布局）
8、setGridSize() -- 设置网格尺寸
9、setSpacing() -- 设置项之间的间隔（此项和上一项互斥）
10、setWordWrap() -- 设置项中的文字是否自动换行；即使启用换行，单元格也不会扩展为文本腾出空间，根据视图的textElideMode，它将为无法显示的文本打印省略号
"""
import sys, time
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class list_view(QListView):
    def __init__(self):
        super(list_view, self).__init__()
        # self.setMouseTracking(True)
        # self.setFlow(QListView.LeftToRight)
        # self.setViewMode(QListView.IconMode)
        # self.setResizeMode(QListView.Adjust)
        # self.setLayoutMode(QListView.SinglePass)
        # self.setGridSize(QSize(50, 30))
        # self.setItemAlignment(Qt.AlignRight)
        self.setMovement(QListView.Free)


class list_model(QStandardItemModel):
    def __init__(self):
        super(list_model, self).__init__()
        self.appendRow(QStandardItem(QIcon('./img/xing.png'), '1. Python'))
        self.appendRow(QStandardItem(QIcon('./img/xing.png'), '2. Java'))
        self.appendRow(QStandardItem(QIcon('./img/xing.png'), '3. Go'))
        self.appendRow(QStandardItem(QIcon('./img/xing.png'), '4. C/C++'))
        self.appendRow(QStandardItem(QIcon('./img/xing.png'), '5. C#'))
        self.appendRow(QStandardItem(QIcon('./img/xing.png'), '6. JavaScript'))


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.window_ui()

    def window_ui(self):
        model = list_model()
        view = list_view()
        view.setModel(model)
        button = QPushButton('Test')
        box = QVBoxLayout()
        box.addWidget(view)
        box.addWidget(button)
        self.setLayout(box)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
