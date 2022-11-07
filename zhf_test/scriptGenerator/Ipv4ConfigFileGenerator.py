from ..scriptGenerator.ConfigFileGenerator import ConfigFileGenerator
from zhf_test.common.ConstVariable import LINK_TYPE_SATELLITE_TO_SATELLITE, \
    LINK_TYPE_SATELLITE_TO_GROUNDSTATION, ENTER_AND_TAB, ENTER
import os


class Ipv4ConfigFileGenerator(ConfigFileGenerator):
    def __init__(self, data):
        self.data = data

    def generate(self):
        start_ipv4_address_byte_3 = 1
        total_ipv4_address = "192.168." + str(start_ipv4_address_byte_3) + ".x"
        final_str = "<config>"
        final_str += ENTER_AND_TAB
        netmask = "255.255.255.252"
        # 进行所有的星间链路的遍历
        for index, link in enumerate(self.data.allLinks.linkSet):
            if link.linkType == LINK_TYPE_SATELLITE_TO_SATELLITE:
                final_str += "<interface among='{}' address='{}' netmask='{}' />" \
                    .format(link.srcNode.sat_name + " " + link.destNode.sat_name, total_ipv4_address, netmask)
            if index == len(self.data.allLinks.linkSet) - 1:
                final_str += ENTER
            else:
                final_str += ENTER_AND_TAB
        final_str += "</config>"
        return final_str

    def writeIntoConfigFile(self, generate_file_path=""):
        generate_file_path = "./" + self.data.projectName + "/masterNodes/" + "address.xml"
        super(Ipv4ConfigFileGenerator, self).writeIntoConfigFile(generate_file_path)
