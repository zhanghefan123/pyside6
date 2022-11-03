# 特定用途的对话框
# 5. QFileDialog -- 文件对话框
"""
QFileDialog常用api：
1、setViewMode() -- 设置对话框的视图模式
    QFileDialog.Detail：显示目录中每个项目的图标、名称和详细信息
    QFileDialog.List：仅显示目录中每个项目的图标和名称

2、setFileMode() -- 设置文件模式，用户可以选择哪些文件
    QFileDialog.AnyFile：任何文件，无论它是否存在
    QFileDialog.ExistingFile：现有的单个文件
    QFileDialog.Directory：目录
    QFileDialog.ExistingFiles：现有的多个文件

3、setAcceptMode() -- 设置对话框类型（用于打开文件还是保存文件），两个值：QFileDialog.AcceptOpen、QFileDialog.AcceptSave
4、setOption() -- 选项设置
    QFileDialog.ShowDirsOnly：仅在文件对话框中显示目录；默认情况下，同时显示文件和目录（仅在Directory文件模式下有效）
    QFileDialog.DontResolveSymlinks：不要解析文件对话框中的符号链接，默认情况下，符号链接得到解决
    QFileDialog.DontConfirmOverwrite：不要要求确认是否选择了现有文件，默认情况下，请求确认（注：此项在在macOS中无效）

5、setNameFilter() -- 设置过滤器
6、setDirectory() -- 设置对话框中的初始目录


QFileDialog常用信号：
1、currentChanged -- 切换选择的文件和目录时都会触发
2、directoryEntered -- 进入目录或离开目录时都会触发
3、fileSelected -- 选定了单个文件或目录时会触发
4、filesSelected -- 选定单个文件、多个文件、目录时都会触发
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
        button = QPushButton('File')
        box = QHBoxLayout()
        box.addWidget(button)
        self.setLayout(box)
        button.clicked.connect(self.window_event)

    def window_event(self):
        file_dialog = QFileDialog(self, 'file_dialog')
        file_dialog.setAcceptMode(QFileDialog.AcceptOpen)
        # file_dialog.setOption(QFileDialog.DontConfirmOverwrite)
        # file_dialog.setNameFilter('(*.py *.doc)')
        # file_dialog.setFileMode(QFileDialog.Directory)

        # file_dialog.filesSelected.connect(self.do_something)
        print(file_dialog.exec())

    def do_something(self):
        print('hello world')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
