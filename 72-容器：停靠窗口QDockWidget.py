# QDockWidget -- 停靠窗口（注意：只能用于主窗口）
"""
QDockWidget常用api：
1、setAllowedAreas() -- 设置控件能停靠的位置，有如下值可用：
    Qt.AllDockWidgetAreas：所有位置都可停靠
    Qt.TopDockWidgetArea：可停靠上方
    Qt.BottomDockWidgetArea：可停靠下方
    Qt.LeftDockWidgetArea：可停靠左侧
    Qt.RightDockWidgetArea：可停靠右侧

2、setFeatures() -- 控件"多功能"设置，有如下值可用：
    QDockWidget.DockWidgetClosable：停靠控件可以关闭；在某些系统上，控件在浮动时始终具有关闭按钮（例如，在MacOS 10.5上）
    QDockWidget.DockWidgetMovable：可以移动停靠控件
    QDockWidget.DockWidgetFloatable：控件可以与主窗口分离，并作为独立窗口浮动
    QDockWidget.DockWidgetVerticalTitleBar：控件在其左侧显示垂直标题栏
    QDockWidget.AllDockWidgetFeatures：可以关闭，移动和浮动控件；相当于上面前三项功能的组合，不过由于将来的发行版中可能会添加新功能，因此，如果使用此项，则控件的外观和行为可能会更改，官方并不推荐使用这项，更推荐使用上面几项的组合来进行设置
    QDockWidget.NoDockWidgetFeatures：控件无法关闭，移动或浮动

3、setFloating() -- 设置控件处于浮动状态
4、setWidget() -- 往停靠窗口中加入其他控件
5、setTitleBarWidget() -- 往停靠窗口标题处加入其他控件
6、allowedAreas() -- 返回控件当前停靠位置
7、isAreaAllowed() -- 判断控件是否处于某个位置
8、isFloating() -- 判断控件是否处于浮动状态


QDockWidget常用信号：
1、allowedAreasChanged -- 控件允许停靠的位置改变时会触发
2、dockLocationChanged -- 控件位置发生改变时会触发（停靠位置变化、停靠转浮动、浮动转停靠）
3、featuresChanged -- 控件功能改变时会触发
"""
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class new_text(QTextEdit):
    def __init__(self):
        super(new_text, self).__init__()
        self.setFrameShape(QFrame.NoFrame)
        self.resize(QSize(100, 70))


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.window_ui()

    def window_ui(self):
        self.resize(QSize(500, 500))
        dock1 = QDockWidget('the test dock1..')
        dock2 = QDockWidget('the test dock2..')
        dock1.setAllowedAreas(Qt.TopDockWidgetArea | Qt.BottomDockWidgetArea)
        dock2.setAllowedAreas(Qt.AllDockWidgetAreas)
        # dock1.setTitleBarWidget()
        self.addDockWidget(Qt.TopDockWidgetArea, dock1)
        self.addDockWidget(Qt.TopDockWidgetArea, dock2)
        # dock1.setFeatures(QDockWidget.DockWidgetVerticalTitleBar)
        # dock1.setFloating(True)
        cw = QWidget()
        self.setCentralWidget(cw)

        text_edit1 = new_text()
        text_edit2 = new_text()
        dock1.setWidget(text_edit1)
        dock2.setWidget(text_edit2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
