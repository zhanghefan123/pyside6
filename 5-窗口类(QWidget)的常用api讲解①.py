# QMainWindow -- 该类可用于创建"主窗口"，主窗口可以包含菜单栏和工具栏
# QDialog -- 该类用于创建对话类型的普通窗口(用于执行短期任务的窗口)
# QWidget -- 如果窗口用途不是很明确，则可以使用该类创建普通窗口；注意，该类是上面两个类的父类

"""
窗口控件（QWidget）主要api：
大小和位置相关：
1、x()和y() -- 控件相对于父级控件的位置，如果没有父级控件，则相对于桌面的位置
2、pos() -- x和y的组合
3、width()和height() -- 控件的宽度和高度
4、size() -- width和height的组合
5、geometry() -- 返回Rect(x, y, width, height)
6、frameSize() -- 包含框架的窗口尺寸
7、frameGeometry() -- 返回包含框架的Rect(x, y, width, height)

8、move(x, y) -- 移动控件到相对于父级控件的绝对位置
9、resize(width, height) -- 设置宽度和高度，不包含框架；（此方法等同于setFixedSize(width, height)）
10、setGeometry(x, y, width, height)
"""
import sys
from PySide6.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.window_ui()

    def window_ui(self):
        button1 = QPushButton('Open')
        button2 = QPushButton('Cannel')
        hbox = QHBoxLayout()
        hbox.addWidget(button1)
        hbox.addWidget(button2)
        self.setLayout(hbox)
        button1.clicked.connect(self.window_event)

    def window_event(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
