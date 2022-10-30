# QDate -- 日期对象
"""
常用api：
1、addDays()、addMonths()、addYears() -- 增加或减少days、months、years
2、day()、month()、year() -- 返回对象中的day数、month数、year数
3、dayOfWeek()、dayOfYear() -- 返回QDate那天是星期几，在那年是第几天
4、daysInMonth()、daysInYear() -- 返回QDate所在的那个月或那一年各有多少天
5、getDate() -- 返回一个由年、月、日组成的元组
6、setDate() -- 设置或修改日期
7、weekNumber() -- 返回QDate所处的那周在当年是多少周
8、toString() -- 将QDate转换成字符串

    d      --- 以数字形式表示的天数，没有前置的零(1~31)
    dd     --- 以数字形式表示的天数，有前置的零(01~31)
    ddd    --- 本地化日期的缩写，例如：周一
    dddd   --- 本地化日期的长名称，例如：星期一
    M      --- 以数字形式表示的月份，没有前置的零(1~12)
    MM     --- 以数字形式表示的月份，有前置的零(01~12)
    MMM    --- 本地化月份的缩写名称，例如，Jan到Dec
    MMMM   --- 本地化的长月份名称，例如，January到December
    yy     --- 以两位数字表示的年份
    yyyy   --- 以4位数字表示的年份


9、daysTo() -- 返回两个QDate之间的间隔天数


静态函数：
1、currentDate() -- 返回当前的QDate
2、fromString() -- 将日期字符串转换成QDate
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
        label = QLabel('测试用...')
        box = QHBoxLayout()
        box.addWidget(label)
        self.setLayout(box)

        date = QDate(2021, 11, 14)
        # date.setDate(2022, 5, 25)
        # print(date.toString('yyyy MMM:dd'))
        # print(date.daysInYear())
        # print(date.daysTo(QDate(2022, 4, 30)))
        # print(QDate.fromString('2022-4-04','yyyy-MM-dd'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
