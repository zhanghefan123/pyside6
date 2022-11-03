# qt处理"事件"的完整流程
"""
步骤：
1、操作系统接收到了用户或程序的请求，判断请求来自于哪个应用程序，于是将请求转发到相应的应用程序
2、应用程序接收到请求后，判断出这是一个事件，于是：①调用QEvent（qt中所有事件类的抽象基类），QEvent根据事件类型调用与事件相关的子事件类创建一个事件对象；②应用程序的notify方法将事件传递到QObject类的event()
3、QObject类的event()并不处理事件，继续将事件传递给相关控件（事件在哪个控件上产生的，就传给哪个控件）的event()
4、控件的event()也不处理事件，继续将事件传递给相应的"事件处理函数"处理

    事件处理函数 -- 事件类中以Event结尾的"虚函数"（通常在事件类文档中可查到，如果查不到，则事件处理函数的名字与事件类的名字一致，只是少了前面的Q）
    * 重写事件处理函数时必须创建新的控件类，继承原控件类，在新类中重写
"""
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class my_lineedit(QLineEdit):
    # 事件处理函数进行最终的处理
    # 事件处理函数是事件类之中以Event结尾的虚函数
    def mousePressEvent(self, event):
        # event 拥有不同的类型，不同的类型之中包含不同的了一些相关的信息
        print(type(event)) # 这里是QMouseEvent，我们可以上网进行查找其中包含什么样的信息
        if event.button() == Qt.LeftButton:
            self.setText('hello world')

    def enterEvent(self, event):
        print('hello')


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.window_ui()

    def window_ui(self):
        line_edit = my_lineedit()
        box = QHBoxLayout()
        box.addWidget(line_edit)
        self.setLayout(box)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
