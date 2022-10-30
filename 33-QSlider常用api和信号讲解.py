# QSlider -- 滑动条
"""
QSlider常用api：
1、setMaximum()、setMinimum() -- 设置最大值和最小值
2、setRange() -- 设置值的范围
3、maximum()、minimum() -- 返回最大值和最小值
4、setSingleStep() -- 设置步长；鼠标点击时前进的步数
5、setPageStep() -- 设置步长；按键盘键时前进的步数
6、setValue() -- 设置滑块的当前值
7、value() -- 返回滑块的当前值
8、setTracking() -- 设置跟踪（默认为开启跟踪）；如果设置了跟踪，则只要拖动滑块，就会触发valueChanged信号，如果不设置跟踪，则只有在松开滑块时会触发valueChanged信号
9、setSliderDown() -- 设置滑块被按下，此方法会触发sliderPressed信号
10、setInvertedAppearance() -- 反向显示；拖动滑块的方向与正常的相反
11、setInvertedControls() -- 反向控制；pgUp为值变小，pgDown为值变大
12、setSliderPosition() -- 设置滑块的位置
13、setOrientation() -- 设置滑动条显示形式，只有两种：Qt.Horizontal（水平）、Qt.Vertical（垂直）

14、setTickPosition() -- 设置滑动条标尺刻度的显示位置，有如下的枚举值可用：

    QSlider.NoTicks：没有刻度
    QSlider.TicksBothSides：在两侧都显示刻度
    QSlider.TicksAbove：在上方显示刻度
    QSlider.TicksBelow：在下方显示刻度
    QSlider.TicksLeft：在左侧显示刻度
    QSlider.TicksRight：在右侧显示刻度

15、setTickInterval() -- 设置刻度之间的间隔


QSlider常用信号：
1、rangeChanged -- 取值范围发生改变时会触发
2、sliderMoved -- 当滑块移动时会触发
3、sliderPressed -- 当滑块被按下时会触发
4、sliderReleased -- 当滑块被释放时会触发
5、valueChanged -- 当滑动条的值发生改变时会触发；如果设置了不跟踪，移动滑块时不会触发，在释放滑块时会触发
"""
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        button = QPushButton('Test')
        self.slider = QSlider()
        box = QVBoxLayout()
        box.addWidget(self.slider)
        box.addWidget(button)
        self.setLayout(box)

        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setRange(0, 100)
        # self.slider.setTracking(False)
        # self.slider.setTickPosition(QSlider.TicksAbove)
        # self.slider.setTickInterval(25)
        # self.slider.setInvertedAppearance(True)
        # self.slider.setSingleStep(3)

        # self.slider.sliderMoved.connect(self.window_event)
        # self.slider.sliderReleased.connect(self.window_event)
        # self.slider.valueChanged.connect(self.slider_event)
        self.slider.sliderPressed.connect(self.slider_event)
        button.clicked.connect(self.button_event)


    def slider_event(self):
        # print(self.slider.value())
        print('hello world')

    def button_event(self):
        print(self.slider.value())
        # self.slider.setSliderDown(True)
        # self.slider.setSliderPosition(34)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
