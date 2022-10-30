# 关于"模型类" -- qt中模型的抽象基类QAbstractItemModel
"""
官方文档描述：

1. QAbstractItemModel为数据提供了接口，这使得数据本身并不需要存放在模型中，而是可以存放在数据结构、某一个单独的类、文件、数据库、或者其它一些应用组件中
2. QAbstractItemModel同时也定义了使用视图和委托来访问数据的接口，对接视图和委托的接口足够的灵活，可以将数据分层进行处理，满足不同的视图呈现方式（列表、表格、树）

要注意的事儿：

* 不要直接使用QAbstractItemModel实例化创建模型，应该使用它的子类（QStandardItemModel）
* 如果当前模型类不能满足需求，可以自定义模型类，不过不要直接继承QAbstractItemModel，应该继承它的子类
"""