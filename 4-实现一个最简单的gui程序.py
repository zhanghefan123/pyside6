# 第一个gui程序
"""
1、使用QApplication类创建应用程序对象；该类管理图形用户界面应用程序的控制流和主要设置；可以说QApplication类是Qt整个后台管理的命脉
2、实例化“主窗口”，并显示（show）它；
注意：不要直接使用控件类实例化创建控件，要创建新类并继承控件类，再使用新类实例化创建控件
3、执行app的主循环
"""
import sys
from PySide6.QtWidgets import *


class Window(QWidget):
    pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
