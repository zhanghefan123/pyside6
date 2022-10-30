# 自定义信号
"""
步骤：
1. 创建控件的子类
2. 在类的最开始通过实例化Signal类创建信号（注：可定义信号的参数）
3. 调用信号的emit方法发射信号（注：可定义信号的触发方式）
注：最好将自定义信号的和现有信号或事件绑定，联动触发
"""
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class my_line_edit(QLineEdit):
    getText = Signal(str)

    def __init__(self):
        super(my_line_edit, self).__init__()
        # self.returnPressed.connect(self.send)

    # def send(self):
    #     self.getText.emit(self.text())

    def mousePressEvent(self, e):
        self.getText.emit(self.text())


class my_button(QPushButton):
    def mousePressEvent(self, e):
        print('world')
        return super(my_button, self).mousePressEvent(e)


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        line_edit = my_line_edit()
        button = my_button()
        button.setText('Test')
        box = QVBoxLayout()
        box.addWidget(line_edit)
        box.addWidget(button)
        self.setLayout(box)

        def do_something():
            print('hello world')

        line_edit.getText.connect(self.window_event)
        button.clicked.connect(do_something)

    def window_event(self, text):
        print(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
