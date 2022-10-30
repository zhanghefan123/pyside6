# 关于自定义委托
"""
回顾一些内容：

1. 委托的作用：负责模式和视图间的交互（提供编辑功能、将数据项渲染成一定的样式再交给视图）
2. Qt中，委托的抽象基类是QAbstractItemDelegate，它定义了通用的接口
3. 它有两个子类：QStyledItemDelegate（默认）、QItemDelegate；它们的区别是：QStyledItemDelegate使用当前样式来渲染数据项，即如果程序设置了总体的样式风格（用QSS或其他定义方式），QStyledItemDelegate会使用这个风格设置


如果要自定义委托，需要重写一些关键的接口，包括：
1. createEditor() -- 创建自定义的控件，并返回之
2. setEditorData() -- 将模型中设置好的数据项的值设置到自定义的控件中
3. setModelData() -- 将自定义控件上的值传递给模型
4. updateEditorGeometry() -- 设置自定义控件在视图中的位置和大小


涉及的一些参数的解释：

* parent -- 委托提供的控件的父级控件
* option -- 类型是QStyleOptionViewItem；视图上的项目的样式的选项，其中包含了项目所有的样式信息，例如大小、位置、颜色、背景等等
* index -- 项目对应的索引
* editor -- 委托提供的控件
* model -- 模型

"""
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class delegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        spin_box = QSpinBox(parent)
        spin_box.setMinimum(0)
        spin_box.setMaximum(100)
        spin_box.setAlignment(Qt.AlignRight)
        return spin_box

    def setEditorData(self, editor, index):
        value = index.data()
        editor.setValue(int(value))

    def setModelData(self, editor, model, index):
        value = editor.value()
        model.setData(index, value)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)


class View(QTableView):
    def __init__(self):
        super(View, self).__init__()
        spin_delegate = delegate()
        self.setItemDelegateForColumn(2, spin_delegate)


class Model(QStandardItemModel):
    def __init__(self):
        super(Model, self).__init__()
        self.setHorizontalHeaderLabels(['物品', '单价', '数量'])
        self.appendRow([QStandardItem('iPhone X'), QStandardItem('8000'), QStandardItem('0')])
        self.appendRow([QStandardItem('iPhone 6'), QStandardItem('3000'), QStandardItem('0')])
        self.appendRow([QStandardItem('MacBook Air'), QStandardItem('10000'), QStandardItem('0')])


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.window_ui()

    def window_ui(self):
        _model = Model()
        _view = View()
        _view.setModel(_model)
        button = QPushButton('Test')
        box = QGridLayout()
        box.addWidget(_view, 0, 0, 3, 1)
        box.addWidget(button, 3, 0, 1, 1)
        self.setLayout(box)

        # self.setFixedWidth(100)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
