# QComboBox -- 下拉列表；也被称为"组合框"，由表单和列表组合而来
"""
QComboBox常用api：
1、addItem()、addItems()、insertItem()、insertItems() -- 往列表中插入"项"；注：索引从0开始
2、setItemText() -- 修改列表项的文本
3、setEditable() -- 设置列表项"可编辑"，设置后列表项变得可编辑，按回车可将修改后的列表项加入下拉列表
4、setEditText() -- 列表项可编辑前提，设置列表项上的文本
5、setItemText()、setItemIcon() -- 设置指定项的文本和图标
6、clearEditText() -- 列表项可编辑前提，清空列表项上的文本
7、removeItem() -- 移除指定的项
8、clear() -- 清除所有项
9、currentText() -- 返回当前选择的项的文本
10、count() -- 返回列表项数量
11、setCurrentText() -- 列表项可编辑前提，设置当前项的文本为指定文本
12、setCurrentIndex() -- 切换到指定索引位置的项，如果不存在此索引的项，则显示空
13、setMaxCount() -- 设置列表项的数量上限
14、setDuplicatesEnabled() -- 设置是否允许有重复的项
15、setIconSize() -- 设置项的图标尺寸
16、setInsertPolicy() -- 列表项可编辑前提，设置编辑列表项后插入列表时的策略

    QComboBox.NoInsert：该文本不会插入到下拉列表中
    QComboBox.InsertAtTop：该文本会作为列表项在列表的第一项插入
    QComboBox.InsertAtCurrent：新输入的文本将会替代当前列表项
    QComboBox.InsertAtBottom：该文本会作为列表项在列表的最后一项插入
    QComboBox.InsertAfterCurrent：该文本会在当前列表项的下一项插入
    QComboBox.InsertBeforeCurrent：该文本会在当前列表项的前面插入
    QComboBox.InsertAlphabetically：该文本将按字母顺序插入下拉列表中

17、 setLineEdit()、lineEdit() -- 设置表单以及获取表单


QComboBox常用信号：
1、currentIndexChanged -- 用户交互，或者以代码的方式，当选择的项发生改变时都会触发
2、activated -- 当用户交互时选择的项发生改变时会触发
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
        self.combox = QComboBox()
        button = QPushButton('Test')
        box = QHBoxLayout()
        box.addWidget(self.combox)
        box.addWidget(button)
        self.setLayout(box)

        self.combox.addItems(['python', 'java', 'c\c++'])
        self.combox.setEditable(True)

        button.clicked.connect(self.window_event)

    def window_event(self):
        # print(self.combox.currentText())
        self.combox.setCurrentText('hello')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
