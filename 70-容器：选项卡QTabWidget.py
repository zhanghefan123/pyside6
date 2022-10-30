# QTabWidget -- 选项卡；可在一个页面中展示多个窗口
"""
QTabWidget常用api：
1、addTab() -- 添加选项卡（窗口）
2、clear() -- 删除所有选项卡，保留选项卡框架
3、count() -- 返回选项卡数量
4、currentIndex() -- 返回当前选项卡索引号（索引从0开始）
5、currentWidget() -- 返回当前选项卡中的窗口
5、insertTab() -- 在指定索引位置添加选项卡（窗口）
6、isMovable()、isTabEnabled()、isTabVisible() -- 判断是否可移动、是否可用、是否可见
7、removeTab() -- 删除指定选项卡
8、setDocumentMode() -- 设置选项卡使用"文档模式"，设置此属性后，不会呈现选项卡的框架，此模式对于显示文档类型页面很有用
9、setIconSize() -- 设置选项卡栏中的图片的大小
10、setMovable() -- 设置选项卡可移动
11、setTabBar() -- 设置自定义的选项卡（关联QTabBar类）
12、setTabBarAutoHide() -- 设置选项卡自动隐藏（如果选项卡数量小于2，则隐藏选项卡）
13、setTabEnabled() -- 设置选项卡是否可用
14、setTabToolTip() -- 设置指定选项卡的提示信息
15、setTabVisible() -- 设置选项卡是否可见（不可见并不影响其他选项卡的索引）
16、setTabsClosable() -- 为选项卡添加关闭按钮
17、setUsesScrollButtons() -- 设置是否在选项卡中添加滚动按钮；当选项卡中的页面太多，而窗口装不下时，滚动按钮会出现，方便通过滚动按钮来滚动选项卡


QTabWidget常用信号：
1、currentChanged -- 当前选项卡状态发生变化时会触发（切换选择、移动、隐藏、移除...）
2、tabBarClicked -- 单击选项卡时触发
3、tabBarDoubleClicked -- 双击选项卡时触发
4、tabCloseRequested -- 点击选项卡上的关闭按钮时会触发
"""
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class test_widge(QWidget):
    def __init__(self):
        super(test_widge, self).__init__()
        button1 = QCheckBox('Python')
        button2 = QCheckBox('Java')
        button3 = QCheckBox('C/C++')
        box = QVBoxLayout()
        box.addWidget(button1)
        box.addWidget(button2)
        box.addWidget(button3)
        self.setLayout(box)


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.window_ui()

    def window_ui(self):
        self.tab = QTabWidget()
        button = QPushButton('Test')
        box = QHBoxLayout()
        box.addWidget(self.tab)
        box.addWidget(button)
        self.setLayout(box)

        test1 = test_widge()
        test2 = test_widge()
        test3 = test_widge()
        self.tab.addTab(test1, QIcon('./img/xing.png'), 'test1...')
        self.tab.addTab(test2, 'test2...')
        self.tab.addTab(test3, 'test3...')

        # self.tab.setDocumentMode(True)
        # self.tab.setTabBarAutoHide(True)
        self.tab.setMovable(True)
        # self.tab.setTabEnabled(0, False)

        self.tab.setTabToolTip(1, 'hello world..')
        self.tab.setTabsClosable(True)

        def do_something():
            print('hello world')

        button.clicked.connect(self.window_event)
        self.tab.tabBarClicked.connect(do_something)

    def window_event(self):
        # self.tab.removeTab(0)
        self.tab.clear()

        print(self.tab.currentIndex())
        # print(self.tab.currentWidget())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
