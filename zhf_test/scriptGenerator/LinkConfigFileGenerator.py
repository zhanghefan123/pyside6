from zhf_test.scriptGenerator.ConfigFileGenerator import ConfigFileGenerator
from zhf_test.common.ConstVariable import *
import os


class LinkConfigFileGenerator(ConfigFileGenerator):
    def __init__(self, data):
        self.data = data

    def generate(self) -> str:
        final_str = "<config>"
        final_str += ENTER_AND_TAB
        for index, link in enumerate(self.data.allLinks.linkSet):
            if link.linkType == LINK_TYPE_SATELLITE_TO_SATELLITE:
                final_str += "<{} src-module='{}' src-gate='{}' dest-module='{}' dest-gate='{}' " \
                             "channel-Type='xxx' linkInfo='xxx'/>". \
                    format(link.linkTypeStr, link.srcNode.sat_name,
                           link.node1EthNum, link.destNode.sat_name, link.node2EthNum)
            elif link.linkType == LINK_TYPE_SATELLITE_TO_GROUNDSTATION:
                final_str += "<{} src-module='{}' src-gate='{}' dest-module='{}' dest-gate='{}' " \
                             "channel-Type='xxx' linkInfo='xxx'/>". \
                    format(link.linkTypeStr, link.srcNode.sat_name,
                           link.node1EthNum, link.destNode.groundStationName, link.node2EthNum)
            if index == len(self.data.allLinks.linkSet) - 1:
                final_str += ENTER
            else:
                final_str += ENTER_AND_TAB
        final_str += "</config>"
        return final_str

    def writeIntoConfigFile(self, generate_file_path=""):
        generate_file_path = "./" + self.data.projectName + "/masterNodes/" + "link_config.xml"
        super(LinkConfigFileGenerator, self).writeIntoConfigFile(generate_file_path)
