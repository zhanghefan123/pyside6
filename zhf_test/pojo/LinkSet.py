from zhf_test.pojo.Link import Link


class LinkSet:
    """
    进行所有的link的存储
    """

    def __init__(self):
        # 这里不需要传入data，因为LinkSet就在data之中
        self.linkSet = []

    def getLinkCount(self):
        """
        返回链路的总的数量
        :return: 返回链路的总的数量
        """
        return len(self.linkSet)

    def addLink(self, node1Type: int, node1Index: int, node2Type: int, node2Index: int, bandwidth):
        """
        添加链路
        :param node1Type: 结点1的类型
        :param node1Index: 结点1的索引
        :param node2Type: 结点2的类型
        :param node2Index: 结点2的索引
        :param data: 公共数据
        :param bandwidth: 带宽
        """
        # 我们需要确保是从卫星发起的链路
        if node1Type > node2Type:
            node1Type, node2Type = node2Type, node1Type
            node1Index, node2Index = node2Index, node1Index
        # 进行link的创建
        link = Link(self.getLinkCount(), node1Type, node1Index, node2Type, node2Index, bandwidth)
        self.linkSet.append(link)

    def findLink(self, node1Type, node1Index, node2Type, node2Index) -> bool:
        if node1Type > node2Type:
            node1Type, node2Type = node2Type, node1Type
            node1Index, node2Index = node2Index, node1Index
        # 遍历所有的link进行查找
        for link in self.linkSet:
            if link.checkIfSameLink(node1Type, node1Index, node2Type, node2Index):
                return True
