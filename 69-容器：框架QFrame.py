# QFrame -- 框架（容器外围的框线就是由这个类来进实现的）；可以包裹多种控件，并设置框线样式
"""
QFrame常用api：
1、setFrameShape() -- 设置框线形状

    QFrame.NoFrame：什么都不画
    QFrame.Box：在周围画一个盒子
    QFrame.Panel：绘制一个面板，使内容看起来凸起或下沉
    QFrame.StyledPanel：绘制矩形面板，其外观取决于当前程序的样式，它可以抬起或下沉
    QFrame.HLine：画一条水平线（用作分隔符）
    QFrame.VLine：画一条垂直线（用作分隔符）
    QFrame.WinPanel：绘制一个矩形面板，可以像Windows 2000那样凸起或下沉；指定此形状将线宽设置为2像素，为了兼容性，为了风格的独立性，我们建议改用它

2、setFrameShadow() -- 设置框线阴影

    QFrame.Plain：与周围环境齐平（没有任何3D效果）
    QFrame.Raised：框架和内容显示凸起
    QFrame.Sunken：框架和内容显示下沉

3、setLineWidth() -- 设置线宽
4、setMidLineWidth() -- 设置中心线的宽度

"""
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.window_ui()

    def window_ui(self):
        self.resize(QSize(300, 300))
        frame = QFrame()
        # label = QLabel('这是一段测试文本')
        box = QHBoxLayout()
        box.addWidget(frame)
        box.addWidget(QPushButton('测试按钮'))
        self.setLayout(box)

        # label.setFrameShape(QFrame.Box)
        # label.setFrameShadow(QFrame.Raised)
        # label.setLineWidth(10)
        # label.setMidLineWidthLineWidth(10)
        frame.setFrameShape(QFrame.Box)
        # frame.setFrameShadow(QFrame.Raised)
        frame.setLineWidth(10)
        frame.setMidLineWidth(10)  # 设置中心线的宽度


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
