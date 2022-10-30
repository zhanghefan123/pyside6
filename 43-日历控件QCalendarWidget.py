# QCalendarWidget -- 日历
"""
QCalendarWidget常用api：
1、setMaximumDate()、setMinimumDate() -- 设置日历显示的最小日期和最大日期
2、setDateRange() -- 设置日历的日期范围
3、maximumDate()、minimumDate() -- 返回日历的最小日期和最大日期
4、selectedDate() -- 返回当前用户选择的日期
5、setDateEditEnabled() -- 让日历支持输入，当日历控件获得焦点时，按非修饰键可弹出一个小型输入框，通过手动输入的方式选择日期（此项默认为True）
6、setDateEditAcceptDelay() -- 设置日历输入时的等待时间（单位是毫秒）
7、setFirstDayOfWeek() -- 设置一周里的第一天；其值为：Qt.DayOfWeek.Monday~Qt.DayOfWeek.Sunday
8、setSelectionMode() -- 设置选择模式，有两个值：QCalendarWidget.SingleSelection（可选择）、QCalendarWidget.NoSelection（不可选择）
9、setSelectedDate() -- 设置日历初始日期
10、monthShown()、yearShown() --  返回当前选择的月份和年份
11、setGridVisible() -- 设置日历网格是否可见
12、setNavigationBarVisible() -- 设置顶部导航是否可见
13、showNextMonth()、showNextYear() -- 分别使日历导航栏中的月份和年份往前进一位
14、showPreviousMonth()、showPreviousYear() -- 分别使日历导航栏中的月份和年份往后退一位

15、setHorizontalHeaderFormat() -- 设置日历水平标题的格式，有四个值：
    QCalendarWidget.SingleLetterDayNames：标题显示日期名称的单字母缩写(例如，星期一为M)
    QCalendarWidget.ShortDayNames：标题显示日期名称的简短缩写(例如，星期一为周一)
    QCalendarWidget.LongDayNames：标题显示完整的日期名称(例如星期一)
    QCalendarWidget.NoHorizontalHeader：标头是隐藏的

16、setVerticalHeaderFormat() -- 设置日历垂直标题的格式，有两个值：
    QCalendarWidget.ISOWeekNumbers：标头显示ISO周编号
    QCalendarWidget.NoVerticalHeader：标头是隐藏的


QCalendarWidget常用信号：
1、clicked -- 在控件中用鼠标单击选择日期时触发
2、activated -- 通过按键盘的Enter键选中日期时触发
3、currentPageChanged -- 在导航栏中切换了年份或者月份时触发
4、selectionChanged -- 在控件中通过键盘的上下左右按钮切换日期时触发
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
        calendar = QCalendarWidget()
        box = QHBoxLayout()
        box.addWidget(calendar)
        self.setLayout(box)

        calendar.setDateRange(QDate(2001, 1, 1), QDate(2035, 12, 31))
        # calendar.setDateEditAcceptDelay(10000)
        # calendar.setDateEditEnabled(False)
        # calendar.setSelectionMode(QCalendarWidget.NoSelection)
        calendar.setNavigationBarVisible(True)
        # calendar.setHorizontalHeaderFormat(QCalendarWidget.SingleLetterDayNames)

        def do_something():
            print(calendar.selectedDate())

        calendar.clicked.connect(do_something)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
