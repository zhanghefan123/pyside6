# 模型/视图 并不是完整的mvc的架构，使用委托来替代控制器的功能
"""
MVC架构 -- 全称是"Model View Controller"，中心思想是：将后台数据和前台的软件界面(也可以称为前端界面)相分离，前后台之间使用特定的控制器来操作数据并进行交互

* Model(存储数据)：模型；是“数据源”，作用是为视图提供要呈现的数据，组织数据的结构
* View(呈现数据)：视图；负责在界面中呈现模型所组织的数据，视图只是在软件界面中提供一个用于呈现数据的框架，它本身不提供数据内容，模型提供什么，它就呈现什么
* Controller：控制器；作用是负责将数据在前后台之间进行传递；在Qt中，使用另一种抽象的对象“Delegate”(委托)来实现Controller的功能

MVC优势：

    1. 在处理较大的数据集时每个控件各司其职，不至于降低性能，如果让界面控件直接加载大量的数据，就会严重拖慢页面的加载速度，使用这种前后端分离的架构能够有效避免这种问题
    2. 一个模型的数据可以映射到多个视图，可以以不同的方式查看同一份数据
    3. 如果底层数据源的存储改变，我们只需要处理模型就可以了，而如果让视图直接加载数据，当有多个这样的视图时，一旦数据有变，就需要去修改所有的视图

    * 数据唯一性（为什么）：如果你界面显示了两份数据，即使你很小心的维护着两份或多份数据保持同步，但你也无法保证数据会时刻保持同步（例如，设计好的两张表中保存了同一份儿数据，当一张表的数据被更新，而另一张表却忘记更新），而且这种情况对于初学者来说也是时有发生
    所以保持数据的唯一性是一个非常重要的话题，而MVC就是这样的一个解决方案，让数据和展示数据的界面相分离，所有数据的更改就通过控制器来实现
"""

# 数据都放在前台会产生什么问题 -- 更新和维护十分繁琐，而且极度容易出错
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.window_ui()

    def window_ui(self):
        text_edit1 = QTextEdit()
        text_edit2 = QTextEdit()
        text_edit1.setHtml('''
        <table border="1"align="center">
			<tr align="center"><th width="100px">name</th><th width="100px">age</th></tr>
			<tr align="center"><td>zhangsan</td><td>30</td></tr>
			<tr align="center"><td>lisi</td><td>32</td></tr>
		</table>
        ''')
        text_edit2.setHtml('''
                <table border="1"align="center">
        			<tr align="center"><th width="100px">name</th><th width="100px">age</th></tr>
        			<tr align="center"><td>zhangsan</td><td>30</td></tr>
        			<tr align="center"><td>lisi</td><td>32</td></tr>
        		</table>
                ''')
        box = QHBoxLayout()
        box.addWidget(text_edit1)
        box.addWidget(text_edit2)
        self.setLayout(box)


if __name__ == '__main__':
    app = QApplication()
    window = Window()
    window.show()
    sys.exit(app.exec())
