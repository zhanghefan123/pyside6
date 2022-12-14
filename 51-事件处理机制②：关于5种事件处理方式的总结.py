# 事件处理方式总结，有下面这几种：
"""
1. 重新实现控件的事件处理函数（最常用） 比如 def keyPressEvent


2. 重新实现notify()(和操作系统相连接的函数)；这个函数的功能强大，提供了完全的控制，可以在事件过滤器得到事件之前就获得它们，但是，它一次只能处理一个事件
(很麻烦)

3. 向QApplication对象上安装事件过滤器；因为一个程序只有一个QApplication对象，实现的功能和notify函数相同，优点是可以同时处理多个事件 (很麻烦)


4. 重写QObject类的event()；QObject类的event()可以在事件到达默认事件处理函数之前获得该事件 (很麻烦)


5. 在父级控件上安装事件过滤器(第二常用的)；使用事件过滤器可以在一个界面类中同时处理不同子控件的事件
"""