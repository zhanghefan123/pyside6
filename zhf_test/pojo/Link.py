class Link:
    def __init__(self, linkId, node1Type, node1Index, node2Type, node2Index, bandwidth):
        """
        :param linkId: 链路的唯一标识
        :param node1Type: 结点1的类型
        :param node1Index: 结点1的索引
        :param node2Type: 结点2的类型
        :param node2Index: 结点2的索引
        :param data: 公共数据
        """
        self.linkId = linkId
        self.node1Type = node1Type
        self.node1Index = node1Index
        self.node2Type = node2Type
        self.node2Index = node2Index
        self.bandwidth = bandwidth
        self.linkInfo = ""
        self.linkType = ""
        self.generateLinkType()
        self.generateLinkInfo()

    def generateLinkType(self):
        if self.node1Type == 1 and self.node2Type == 1:
            self.linkType = "SatToSat"
        elif (self.node1Type == 1 and self.node2Type == 2) or (self.node1Type == 2 and self.node2Type == 1):
            self.linkType = "SatToGround"

    def checkIfSameLink(self, node1Type, node1Index, node2Type, node2Index):
        """
        检测是否是同一条链路
        :param node1Type:
        :param node1Index:
        :param node2Type:
        :param node2Index:
        :return:
        """
        # 如果是非星间链路的情况
        if node1Type == 1 and node2Type == 1:
            if node1Type == self.node1Type and node2Type == self.node2Type \
                    and node1Index == self.node1Index and node2Index == self.node2Index:
                return True
            else:
                return False
        # 如果是星地链路的情况
        elif node1Type == 1 and node2Type == 2:
            if node1Type == self.node1Type and node2Type == self.node2Type \
                    and node1Index == self.node1Index and node2Index == self.node2Index:
                return True
            else:
                return False

    def generateLinkInfo(self) -> None:
        """
        进行链路信息的生成
        """
        if self.linkType == "SatToSat":
            self.linkInfo = "CONS0_SAT_" + str(self.node1Index) + "<-->" + "CONS0_SAT_" + str(self.node2Index) + \
                            ",bandWidth:" + str(self.bandwidth)
        elif self.linkType == "SatToGround":
            self.linkInfo = "CONS0_SAT_" + str(self.node1Index) + "<-->" + "" + str(self.node2Index) + ",bandWidth:" + \
                            str(self.bandwidth)
