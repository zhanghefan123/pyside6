NODE_TYPE_SATELLITE = 1
NODE_TYPE_GROUNDSTATION = 2
LINK_TYPE_SATELLITE_TO_SATELLITE = 3
LINK_TYPE_SATELLITE_TO_GROUNDSTATION = 4
SATELLITE_TYPE = "SatComm"
GROUND_STATION_TYPE = "GroundCommNode"
TAB = "\t"
ENTER_AND_TAB = "\n\t"
ENTER = "\n"
# 进行NED文件提前的导入
PreImportOfNedFile = """
package masterNodes;

import osgNodes.Clock;
import osgNodes.ChannelController;
import osgNodes.GroundNodeMobility;
import osgNodes.GroundCommNode;
import osgNodes.OsgEarthScene;
import osgNodes.SatMobility;
import osgNodes.SatComm;
import osgNodes.SatHost;
import channels.SatToSat;
import channels.SatToGround;
import channels.GroundToGround;
import inet.common.scenario.ScenarioManager;
import inet.common.misc.ThruputMeteringChannel;
import inet.node.ospfv2.OspfRouter;
import inet.networklayer.configurator.ipv4.Ipv4NetworkConfigurator;
import inet.networklayer.ipv4.RoutingTableRecorder;
"""

networkOfNedFile ="""
network OsgEarthNet
{
"""

ParametersAndTypesOfNedFile = """
    parameters:
        @display("bgb=1293.3201,717.0625;bg=black");
        int rngNum = default(5);
        double sendInterval = default(0.1);

    types:
        channel SatToGround_1Gbps extends SatToGround
        {
            datarate = 1Gbps;
        }
        channel SatToSat_10Mbps extends SatToSat
        {
            datarate = 10Mbps;
        }
        channel SatToSat_1Gbps extends SatToSat
        {
            datarate = 1Gbps;
        }
        channel SatToGround_10Mbps extends SatToGround
        {
            datarate = 10Mbps;
        }
"""

NecessarySubmodules = """
    submodules:
        osgEarthScene: OsgEarthScene {
            @display("is=vl;p=127.1975,465.88");
        }
        channelController: ChannelController {
            parameters:
                config = xmldoc("link_config.xml");
                @display("p=115.10876,646.8788");
        }
        clock: Clock {
            @display("p=128.73001,32.182503");
        }
        configurator: Ipv4NetworkConfigurator {
            parameters:
                @display("p=128.73001,107.275;is=s");
                config = xmldoc("./address.xml");
                addStaticRoutes = false;
                addDefaultRoutes = false;
        }
"""
OSPFConfigPre = """
<?xml version="1.0"?>
<OSPFASConfig xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="OSPF.xsd">

  <!-- Areas -->
  <Area id="0.0.0.0">
  </Area>
"""

OSPFConfigEnd = """
</OSPFASConfig>
"""

IniFilePre = """
[General]
# 设置图形界面
user-interface = Qtenv

# 设置背景
*.osgEarthScene.scene = "simple.earth"

# 设置网络
network = OsgEarthNet

# 设置分辨率
simtime-resolution = ms

# 设置信道处理
**.ChannelControllerModule = "channelController"

# ospf的配置文件
**.ospf.ospfConfig = xmldoc("ospf_config.xml")

# 进行统一的卫星的参数的设置
*.sat*.mobility.labelColor ="#ffff00ff"
*.sat*.mobility.typename ="SatMobility"
*.sat*.mobility.modelURL="satellite.osgb"
*.sat*.mobility.modelScale=78000


# 进行统一的地面站的参数的设置
*.GND*.mobility.labelColor ="#ffff00ff"
*.GND*.mobility.typename = "GroundNodeMobility"
*.GND*.mobility.modelURL = "Router higt-poly.obj"
*.GND*.mobility.modelScale = 780000
*.GND*.mobility.altitude = 0.000 km

# 不记录日志
**.statistic-recording = false
**.scalar-recording = false
**.vector-recording = false

"""