# QDateTimeEdit -- 时间日期表单；用于设置时间和日期
"""
常用api：
1、date()、time()、dateTime() -- 返回文本框中对应部分的内容
2、setMaximumDate()、setMinimumDate() -- 设置最大值和最小值；（注：Time和DateTime也有相同的方法）
3、setDateRange() -- 设置范围；（注：Time和DateTime也有相同的方法）
4、setDisplayFormat() -- 设置显示格式（注：需要使用特定的时间和日期字符）
5、maximumDate()、minimumDate() -- 返回最大值和最小值；（注：Time和DateTime也有相同的方法）
6、sectionText() -- 返回由Section对象指定部分的文本，有如下的值：

    NoSection：不对应任何部分
    AmPmSection：对应显示“AM|PM”的部分
    SecondSection：对应秒数的部分
    MinuteSection：对应分钟数的部分
    HourSection：对应小时数的部分
    DaySection：对应天数的部分
    MonthSection：对应月份数的部分
    YearSection：对应年份的部分


7、setCalendarPopup() -- 设置是否允许使用日历来选择日期
8、setCalendarWidget() -- 传递日历
9、setSelectedSection() -- 让光标跳转到由Section对象指定的部分
10、setDate()、setTime()、setDateTime() -- 设置或修改date、time、datetime

常用信号：
1、dateChanged -- 当日期部分发生改变时触发
2、dateTimeChanged -- 当日期和时间发生改变时触发
3、TimeChanged -- 当时间部分发生改变时触发
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
        # dt_edit = QDateTimeEdit(QTime(13, 45, 32))
        dt_edit = QDateTimeEdit(QDateTime(2021, 11, 14, 20, 37, 45))
        # dt_edit.setDateRange()
        dt_edit.setDisplayFormat('yyyy-MM-dd hh:mm:ss')
        button = QPushButton('Ok')
        box = QHBoxLayout()
        box.addWidget(dt_edit)
        box.addWidget(button)
        self.setLayout(box)

        # dt_edit.setDate(QDate(2022, 4, 5))
        # dt_edit.setCalendarPopup(True)

        def window_event():
            # print(dt_edit.sectionText(QDateTimeEdit.YearSection))
            dt_edit.setSelectedSection(QDateTimeEdit.HourSection)

        button.clicked.connect(window_event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
