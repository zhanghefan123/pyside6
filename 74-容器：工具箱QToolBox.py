# QToolBox -- 工具箱；提供一列选项卡式的页面控件，类似"抽屉"的效果
"""
QToolBox常用api：
1、addItem() -- 添加选项卡，并传递选项卡中呈现的控件
2、insertItem() -- 在指定位置添加选项卡，并传递选项卡中呈现的控件
3、count() -- 返回工具箱中选项卡的数量
4、currentIndex() -- 返回当前选项卡的索引
5、currentWidget() -- 返回当前选项卡中的控件
6、removeItem() -- 移除选项卡
7、setItemEnabled() -- 设置选项卡是否可用
8、setItemIcon() -- 设置选项卡的图标
9、setItemText() -- 设置选项卡的文本
10、setItemToolTip() -- 设置选项卡提示语
11、setCurrentIndex() -- 设置当前打开的选项卡（接收索引）
12、setCurrentWidget() -- 设置当前打开的选项卡（接收控件）


QToolBox信号：
1、currentChanged -- 当前选项卡发生改变时会触发（切换、移除、选项卡中控件改变）
"""
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class tool_button(QToolButton):
    def __init__(self, path):
        super(tool_button, self).__init__()
        self.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.setIcon(QIcon(path))
        self.setIconSize(QSize(50, 50))


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.window_ui()

    def window_ui(self):
        tool_box = QToolBox()
        button1 = tool_button('./img/1.jpeg')
        button2 = tool_button('./img/2.jpeg')
        button3 = tool_button('./img/3.jpeg')
        button4 = tool_button('./img/4.jpeg')
        button5 = tool_button('./img/5.jpeg')
        button6 = tool_button('./img/6.webp')
        button_box1 = QVBoxLayout()
        button_box2 = QVBoxLayout()
        group_box1 = QGroupBox()
        group_box2 = QGroupBox()
        button_box1.addWidget(button1)
        button_box1.addWidget(button2)
        button_box1.addWidget(button3)
        button_box2.addWidget(button4)
        button_box2.addWidget(button5)
        button_box2.addWidget(button6)
        group_box1.setLayout(button_box1)
        group_box2.setLayout(button_box2)
        # tool_box.setItemToolTip(1, '我闺蜜')

        but = QPushButton('Test')
        box = QHBoxLayout()
        box.addWidget(tool_box)
        box.addWidget(but)
        self.setLayout(box)

        tool_box.addItem(group_box1, '家人')
        tool_box.addItem(group_box2, QIcon('./img/xing.png'), '闺蜜')

        def window_event():
            # print(tool_box.count())
            # print(tool_box.currentIndex())
            # print(tool_box.currentWidget())
            # tool_box.removeItem(1)
            # tool_box.setItemEnabled(1, False)
            tool_box.setCurrentWidget(group_box2)

        but.clicked.connect(window_event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
