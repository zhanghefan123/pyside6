# 特定用途的对话框
# 6. QProgressDialog -- 进度对话框
"""
QProgressDialog常用api：
1、setMaximum()、setMaximum() -- 设置任务量的最小值和最大值
2、setRange() -- 设置任务量范围
3、setMinimumDuration() -- 设置"预估"的处理时间（单位是毫秒）超过这个事件才会出现进度条（如果不超过这个时间将不会出现进度条）
# 相当于是用户容忍的一个时间
4、setCancelButton() -- 设置一个Cancel按钮
5、setCancelButtonText() -- 设置默认Cancel按钮上的文本
6、setLabel() -- 设置一个标签
7、setLabelText() -- 设置默认标签上的文本
8、setBar() -- 设置一个进度条
9、setValue() -- 设置当前完成的任务量
10、forceShow() -- 如果对话框在算法启动并经过minimumDuration毫秒后仍然隐藏，则显示对话框
11、wasCanceled() -- 监测用户是否点击Cancel按钮，没有单击返回False，单击返回True

* 一定要设置对话框模态，不推荐使用非模态

QProgressDialog常用信号:
1、canceled -- 当点击Cancel按钮时会触发
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
        button = QPushButton('Test...')
        box = QHBoxLayout()
        box.addWidget(button)
        self.setLayout(box)
        button.clicked.connect(self.window_event)

    def window_event(self):
        pg_dialog = QProgressDialog(self)
        # pg_dialog.forceShow()
        pg_dialog.setLabelText('now loading...')
        pg_dialog.setWindowModality(Qt.WindowModal)
        # 不管总的运行时间是否超过了我们的minimumDuration，都会显示进度条
        pg_dialog.forceShow()
        pg_dialog.setRange(0, 10000)
        for i in range(10000):
            pg_dialog.setValue(i)
            # 中途取消
            if pg_dialog.wasCanceled():
                break


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
