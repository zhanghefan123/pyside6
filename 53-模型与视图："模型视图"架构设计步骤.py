# 模型/视图的流程
"""
设计步骤：

1. 创建模型
2. 在模型中指定数据位置，对模型进行设置
3. 创建视图，对视图进行设置
4. 将模型和视图相关联

* 不需要单独创建委托，因为将模型和视图关联的时候，Qt会调用默认的委托对象，默认的委托对象已经能够做得很好，除非你有一些特殊的要求，你才需要自定义委托对象
"""
# 关于"委托"的一些补充 -- 官方文档描述：QAbstractItemDelegate在模型/视图架构中代表抽象的基类；默认的委托实现由QStyledItemDelegate提供，这被Qt
# 的标准视图用作默认的委托，然而，QStyledItemDelegate和QItemDelegate独立替代绘画，且为视图项提供编辑器；它们之间的区别在于QStyledItemDelegate
# 使用当前样式来绘制项目。因此，建议实现自定义委托或当与Qt样式表一起使用时，使用QStyledItemDelegate作为基类





