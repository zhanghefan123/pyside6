# QMdiArea -- MDI窗口管理器；管理区域中可以呈现多个窗口，并以级联或瓷砖模式排列它们
"""
QMdiArea常用api：
1、addSubWindow() -- 往管理器中添加mdi窗口（mdi窗口类型为QMdiSubWindow）
2、removeSubWindow -- 清除指定mdi窗口中的控件，但是保留mdi窗口
3、setViewMode() -- 设置mdi视图模式，有两个值可用：
    QMdiArea.SubWindowView：以子窗口的形式呈现mdi窗口
    QMdiArea.TabbedView：以选项卡的形式呈现mdi窗口

4、setTabsClosable() -- 在选项卡上设置关闭按钮（前提是TabbedView）
5、setTabsMovable() -- 选项卡可移动位置（前提是TabbedView）
6、currentSubWindow() -- 返回当前激活的mdi窗口
7、subWindowList() -- 返回由所有mdi窗口组成的列表
8、setActivationOrder() -- 设置mdi窗口的排序策略，三个枚举值可用：

    QMdiArea.CreationOrder：按传入管理器的顺序排列
    QMdiArea.StackingOrder：按堆叠顺序排列，最上面的mdi窗口是最后一项
    QMdiArea.ActivationHistoryOrder：根据它们最近的激活历史记录排列

9、cascadeSubWindows() -- mdi级联型排列
10、tileSubWindows() -- mdi瓷砖型排列
11、closeActiveSubWindow() -- 关闭mdi窗口
12、closeAllSubWindows() -- 关闭所有的mdi窗口
13、setActiveSubWindow() -- 通过传递mdi窗口来激活它


QMdiArea信号：
1、subWindowActivated -- mdi窗口被激活时就会触发（点击、被创建）
"""
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class my_widget(QWidget):
    def __init__(self, title):
        super(my_widget, self).__init__()
        self.setWindowTitle(title)
        text_edit = QTextEdit()
        box = QHBoxLayout()
        box.addWidget(text_edit)
        self.setLayout(box)


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.window_ui()

    def window_ui(self):
        t1 = my_widget('test1')
        t2 = my_widget('test2')
        t3 = my_widget('test3')
        button = QPushButton('Test')
        box = QVBoxLayout()
        mdi = QMdiArea()
        box.addWidget(mdi)
        box.addWidget(button)
        w = QWidget()
        w.setLayout(box)
        self.setCentralWidget(w)

        mdi.addSubWindow(t1)
        mdi.addSubWindow(t2)
        mdi.addSubWindow(t3)

        # mdi.setDocumentMode(False)
        # mdi.setViewMode(QMdiArea.TabbedView)
        # mdi.setTabsMovable(True)
        # mdi.setTabsClosable(True)

        def window_event():
            print('hello world')
            # mdi.removeSubWindow(t1)
            # print(mdi.subWindowList())
            # mdi.cascadeSubWindows()
            # mdi.setActiveSubWindow()

        button.clicked.connect(window_event)
        # mdi.subWindowActivated.connect(window_event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
