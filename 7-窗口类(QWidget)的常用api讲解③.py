"""
窗口控件（QWidget）主要api：
窗口设置和交互状态、信息提示相关：
1、setWindowIcon() -- 设置窗口图标（只在windows系统中生效）
2、setWindowTitle() -- 设置窗口标题
3、setWindowOpacity(float) -- 设置窗口透明度，其值介于0~1
4、setWindowState(state) -- 设置窗口状态，三个主要的值为：Qt.WindowMaximized、Qt.WindowMinimized、Qt.WindowFullScreen
5、showFullScreen() -- 让窗口全屏
6、showMaximized() -- 让窗口最大化
7、showMinimized() -- 让窗口最小化
8、showNormal() -- 让窗口回复正常大小
9、isFullScreen()、isMaximized()、isMinimized() -- 判断窗口是否全屏、是否最大化、是否最小化
10、windowIcon() -- 返回当前窗口的图片
11、windowTitle() -- 返回当前窗口标题
12、windowOpacity() -- 返回当前窗口透明度

13、setEnabled(bool) -- 设置窗口是否可用
14、setVisible(bool) -- 设置窗口是否可见
15、setHidden(bool) -- 设置窗口是否隐藏
16、close() -- 关闭窗口
17、isEnabled()、isVisible()、isHidden() -- 判断是否可用、是否可见、是否隐藏

18、setStatusTip -- 设置状态栏提示语
19、setToolTip -- 设置窗口上的提示语
20、setLayout -- 往窗口中添加布局
"""
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


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
        self.statusTip()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
