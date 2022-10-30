# 如何定位到具体的控件 -- qss选择器
"""
1、通用选择器 -- *；匹配所有控件
2、类型选择器 -- 例如：QPushButton；匹配QPushButton类及其子类的实例
3、类选择器 -- 例如：[QPushButton].QPushButton；匹配QPushButton类的实例，不包含其子类的实例，也可匹配具有class属性的控件
4、id选择器 -- 例如：[QPushButton]#button；匹配对象名为button的实例（在一个程序中，对象名最好是唯一的）
5、后代选择器 -- 例如：QDialog QPushButton；匹配QDialog中所有QPushButton的实例（子、孙等）
6、子选择器 -- 例如：QDialog > QPushButton；匹配QDialog的直接下一级中所有QPushButton的实例（子）

7、属性选择器 -- 匹配具有指定属性、属性值的类的实例；有如下这些形式：

    (1). [*][attr]：匹配拥有attr属性的实例
    (2). [*][attr='value']：匹配拥有attr属性，并且值等于value的实例
    (3). [*][attr^='value']：匹配拥有attr属性，并且值开头是value的实例
    (4). [*][attr$='value']：匹配拥有attr属性，并且值结尾是value的实例
    (5). [*][attr*='value']：匹配拥有attr属性，并且值中包含value（无论value处于什么位置）的实例


注意：以上的选择器均可：①混用，或者②连接使用（集合选择器）
"""
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


def qss_read(file):
    with open(file) as f:
        return f.read()


class Button(QPushButton):
    pass


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        group_box = QGroupBox()
        group_layout = QVBoxLayout(group_box)
        box = QVBoxLayout(self)
        button1 = QPushButton('button1')
        button2 = QPushButton('button2')
        button3 = Button('button3')
        button4 = Button('button4')
        line_edit1 = QLineEdit()
        line_edit2 = QLineEdit()

        group_layout.addWidget(line_edit1)
        group_layout.addWidget(line_edit2)
        group_layout.addWidget(button4)
        box.addWidget(button1)
        box.addWidget(button2)
        box.addWidget(button3)
        box.addWidget(group_box)

        self.setProperty('class', 'self')
        # print(line_edit1.parent())
        button1.setProperty('class', 'but but1')
        button3.setProperty('class', 'but')
        # line_edit1.setProperty('class', 'but')
        button1.setObjectName('butt')
        line_edit2.setObjectName('butt2')

        button1.setProperty('var', 'test1')
        button2.setProperty('var', 'test2')
        button3.setProperty('var', 'test')
        button4.setProperty('var2', 'test')
        line_edit1.setProperty('var', 'lines')

        self.setStyleSheet(qss_read('qss1.qss'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
