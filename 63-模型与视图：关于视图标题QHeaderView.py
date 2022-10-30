# QHeaderView -- 头部标题视图
"""
QHeaderView常用api：
1、setDefaultSectionSize() -- 设置section的默认尺寸大小
2、setMaximumSectionSize()、setMinimumSectionSize() -- 设置section的最大尺寸和最小尺寸
3、setSectionResizeMode() -- 设置调整标题尺寸大小模式，有四个值可用：

    QHeaderView.Interactive：用户可以手动调整section的大小，也可以使用编程调整大小；section尺寸大小默认为defaultSectionSize
    QHeaderView.Fixed：用户无法手动调整section的大小；只能使用编程调整大小；section尺寸大小默认为defaultSectionSize
    QHeaderView.Stretch：自动调整section的大小以填充可用空间；用户无法更改大小或以编程方式更改大小
    QHeaderView.ResizeToContents：将根据整个列或行的内容自动将section调整为最佳大小；用户无法更改大小或以编程方式更改大小

4、setSectionsMovable() -- 设置section是否可移动（注意：移动并不会影响到模型）
5、setDefaultAlignment() -- 设置标题项文本默认对齐方式
6、hideSection()、showSection() -- 隐藏标题项和显示标题项
7、sectionSize() -- 返回当前标题项尺寸
8、defaultSectionSize() -- 返回标题项的默认尺寸


QHeaderView常用信号：
1、sectionClicked -- 单击或双击标题项时会触发
2、sectionCountChanged -- 标题项数量发生改变时会触发
3、sectionDoubleClicked -- 双击标题项时会触发
5、sectionHandleDoubleClicked -- 双击标题项的边框时会触发
6、sectionMoved -- 当移动标题时会触发
7、sectionPressed -- 按下标题项时就会触发
8、sectionResized -- 标题项尺寸改变时就会触发

"""
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class table_model(QStandardItemModel):
    def __init__(self):
        super(table_model, self).__init__()
        self.setHorizontalHeaderLabels(['name', 'age', 'job'])
        self.appendRow([QStandardItem('zhangsan'), QStandardItem('30'),
                        QStandardItem('软件工程师')])
        self.appendRow([QStandardItem('lisi'), QStandardItem('22'), QStandardItem('测试工程师')])
        self.appendRow([QStandardItem('laowang'), QStandardItem('46'), QStandardItem('网络架构师')])
        self.appendRow([QStandardItem('xiaoming'), QStandardItem('34'), QStandardItem('全栈架构师')])


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.window_ui()

    def window_ui(self):
        _model = table_model()
        # _model = tree_model()
        _view = QTableView()
        # view = QTreeView()
        _view.setModel(_model)
        button = QPushButton('Test')
        box = QVBoxLayout()
        box.addWidget(_view)
        box.addWidget(button)
        self.setLayout(box)

        header = _view.horizontalHeader()
        vheader = _view.verticalHeader()

        # header.setSectionHidden(1, True)
        # print(header.count())
        # header.hideSection(0)
        # vheader.hideSection(0)
        # header.setSectionResizeMode()
        header.setSectionsMovable(True)

        def window_event():
            print(_model.data(_model.index(0, 0)))
            # print(_view.currentIndex())
            # print(header.sectionSize(0))
            # print(header.defaultSectionSize())
            # header.hideSection(0)
            # _model.setHorizontalHeaderLabels(['name', 'age', 'job', 'tel'])

        def do_something():
            print('hello world')

        button.clicked.connect(window_event)
        # header.sectionResized.connect(do_something)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
