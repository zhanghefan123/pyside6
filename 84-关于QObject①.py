# QObject -- qt对象的基类；负责定义qt对象的核心接口，包括：基本信息、行为、核心机制（信号和槽、事件、定时器、翻译等..）
"""
与"对象信息"相关的主要api：
1、setObjectName() -- 设置对象名称
2、objectName() -- 返回对象的名称
3、parent() -- 返回对象的父级对象；（指定谁在谁的里面）
4、children() -- 返回由对象的子对象组成的列表
5、setParent() -- 设置对象的父级对象（注：设置了对象的父级后，对象会转移到父级对象中）
6、setProperty() -- 动态的为对象设置属性（注：可为属性设置多个值）
7、dynamicPropertyNames() -- 返回由对象属性组成的列表
"""
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

def qss_read(file):
    with open(file) as f:
        return f.read()

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        box = QVBoxLayout()
        button = QPushButton('Cancel')
        line_edit = QLineEdit()
        text_edit = QTextEdit()
        box.addWidget(button)
        box.addWidget(line_edit)
        box.addWidget(text_edit)
        self.setLayout(box)

        # button.setParent(line_edit)
        # button.setObjectName('button2')
        # line_edit.setObjectName('button2')
        button.setProperty('class', 'but')
        button.setProperty('var1', 'but')
        button.setProperty('var2', 'but')
        # text_edit.setProperty('class', 'but but1')

        def window_event():
            # print(button.objectName())
            # print(line_edit.objectName())
            # print(button.parent())
            # print(self.children())
            print(button.dynamicPropertyNames())

        button.clicked.connect(window_event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    # window.setStyleSheet(qss_read('test.css'))
    window.show()
    sys.exit(app.exec())
