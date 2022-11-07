from zhf_test.common.ConstVariable import *


class Link:
    def __init__(self, linkId, node1Type, srcNode, node2Type, destNode, bandwidth, constellationName,
                 node1EthNum, node2EthNum, groundStationName):
        """
        :param linkId: 链路的唯一标识
        :param node1Type: 结点1的类型
        :param srcNode: 结点1的索引
        :param node2Type: 结点2的类型
        :param destNode: 结点2的索引
        """
        self.linkId = linkId
        self.node1Type = node1Type
        self.srcNode = srcNode
        self.node2Type = node2Type
        self.destNode = destNode
        self.bandwidth = bandwidth
        self.linkInfo = ""
        self.linkType = ""
        self.linkTypeStr = ""
        self.constellationName = constellationName
        self.groundStationName = groundStationName
        self.generateLinkType()
        self.generateLinkInfo()
        self.node1EthNum = node1EthNum
        self.node2EthNum = node2EthNum

    def generateLinkType(self):
        if self.node1Type == 1 and self.node2Type == 1:
            self.linkType = LINK_TYPE_SATELLITE_TO_SATELLITE
            self.linkTypeStr = "SatToSat"
        elif (self.node1Type == 1 and self.node2Type == 2) or (self.node1Type == 2 and self.node2Type == 1):
            self.linkType = LINK_TYPE_SATELLITE_TO_GROUNDSTATION
            self.linkTypeStr = "SatToGround"

    def checkIfSameLink(self, node1Type, srcNode, node2Type, destNode):
        """
        检测是否是同一条链路
        :param node1Type:
        :param srcNode:
        :param node2Type:
        :param destNode:
        :return:
        """
        # 如果是非星间链路的情况
        if node1Type == 1 and node2Type == 1:
            if node1Type == self.node1Type and node2Type == self.node2Type \
                    and srcNode == self.srcNode and destNode == self.destNode:
                return True
            else:
                return False
        # 如果是星地链路的情况
        elif node1Type == 1 and node2Type == 2:
            if node1Type == self.node1Type and node2Type == self.node2Type \
                    and srcNode == self.srcNode and destNode == self.destNode:
                return True
            else:
                return False

    def generateLinkInfo(self) -> None:
        """
        进行链路信息的生成
        """
        if self.linkType == LINK_TYPE_SATELLITE_TO_SATELLITE:
            self.linkInfo = self.constellationName + "_SAT_" + str(self.srcNode.sat_id) + "<-->" + \
                            self.constellationName + "_SAT_" + str(self.destNode.sat_id) + ",bandWidth:" \
                            + str(self.bandwidth)
        elif self.linkType == LINK_TYPE_SATELLITE_TO_GROUNDSTATION:
            if self.groundStationName == "GND":
                self.linkInfo = self.constellationName + "_SAT_" + str(self.srcNode.sat_id) + "<-->" + \
                                "GND" + str(self.destNode.groundStationId) + ",bandWidth:" + str(self.bandwidth)
            else:
                self.linkInfo = self.constellationName + "_SAT_" + str(self.srcNode.sat_id) + "<-->" + \
                                self.groundStationName + ",bandWidth:" + str(self.bandwidth)


