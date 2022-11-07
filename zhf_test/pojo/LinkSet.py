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

    def addLink(self, node1Type: int, srcNode, node2Type: int, destNode: int, bandwidth, constellationName,
                node1EthNum, node2EthNum, groundStationName=""):
        """
        添加链路
        :param node2EthNum:
        :param node1EthNum:
        :param groundStationName: 地面站的名称
        :param constellationName: 所属星座的名称
        :param node1Type: 结点1的类型
        :param srcNode: 源结点
        :param node2Type: 结点2的类型
        :param destNode: 目的结点
        :param bandwidth: 带宽
        """
        # 我们需要确保是从卫星发起的链路
        if node1Type > node2Type:
            node1Type, node2Type = node2Type, node1Type
            srcNode, destNode = destNode, srcNode
            node1EthNum, node2EthNum = node2EthNum, node1EthNum
        # 进行link的创建
        link = Link(self.getLinkCount(), node1Type, srcNode, node2Type, destNode, bandwidth, constellationName,
                    node1EthNum, node2EthNum, groundStationName)
        self.linkSet.append(link)

    def findLink(self, node1Type, srcNode, node2Type, destNode) -> bool:
        if node1Type > node2Type:
            node1Type, node2Type = node2Type, node1Type
            srcNode, destNode = destNode, srcNode
        # 遍历所有的link进行查找
        for link in self.linkSet:
            if link.checkIfSameLink(node1Type, srcNode, node2Type, destNode):
                return True

