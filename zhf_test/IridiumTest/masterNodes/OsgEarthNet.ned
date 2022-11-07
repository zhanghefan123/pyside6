
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

network OsgEarthNet
{

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

        Iridium_SAT_0: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[3];
        }
        Iridium_SAT_1: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[3];
        }
        Iridium_SAT_2: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[3];
        }
        Iridium_SAT_3: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[3];
        }
        Iridium_SAT_4: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[3];
        }
        Iridium_SAT_5: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[3];
        }
        Iridium_SAT_6: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[3];
        }
        Iridium_SAT_7: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[3];
        }
        Iridium_SAT_8: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[3];
        }
        Iridium_SAT_9: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[3];
        }
        Iridium_SAT_10: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[3];
        }
        Iridium_SAT_11: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[4];
        }
        Iridium_SAT_12: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[4];
        }
        Iridium_SAT_13: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[4];
        }
        Iridium_SAT_14: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[4];
        }
        Iridium_SAT_15: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[4];
        }
        Iridium_SAT_16: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[4];
        }
        Iridium_SAT_17: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[4];
        }
        Iridium_SAT_18: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[4];
        }
        Iridium_SAT_19: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[4];
        }
        Iridium_SAT_20: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[4];
        }
        Iridium_SAT_21: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[4];
        }
        Iridium_SAT_22: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[4];
        }
        Iridium_SAT_23: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[4];
        }
        Iridium_SAT_24: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[4];
        }
        Iridium_SAT_25: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[4];
        }
        Iridium_SAT_26: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[4];
        }
        Iridium_SAT_27: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[4];
        }
        Iridium_SAT_28: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[4];
        }
        Iridium_SAT_29: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[4];
        }
        Iridium_SAT_30: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[4];
        }
        Iridium_SAT_31: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[4];
        }
        Iridium_SAT_32: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[4];
        }
        Iridium_SAT_33: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[4];
        }
        Iridium_SAT_34: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[4];
        }
        Iridium_SAT_35: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[4];
        }
        Iridium_SAT_36: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[4];
        }
        Iridium_SAT_37: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[4];
        }
        Iridium_SAT_38: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[4];
        }
        Iridium_SAT_39: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[4];
        }
        Iridium_SAT_40: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[4];
        }
        Iridium_SAT_41: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[4];
        }
        Iridium_SAT_42: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[4];
        }
        Iridium_SAT_43: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[4];
        }
        Iridium_SAT_44: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[4];
        }
        Iridium_SAT_45: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[4];
        }
        Iridium_SAT_46: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[4];
        }
        Iridium_SAT_47: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[4];
        }
        Iridium_SAT_48: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[4];
        }
        Iridium_SAT_49: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[4];
        }
        Iridium_SAT_50: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[4];
        }
        Iridium_SAT_51: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[4];
        }
        Iridium_SAT_52: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[4];
        }
        Iridium_SAT_53: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[4];
        }
        Iridium_SAT_54: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[4];
        }
        Iridium_SAT_55: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[3];
        }
        Iridium_SAT_56: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[3];
        }
        Iridium_SAT_57: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[3];
        }
        Iridium_SAT_58: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[3];
        }
        Iridium_SAT_59: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[3];
        }
        Iridium_SAT_60: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[3];
        }
        Iridium_SAT_61: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[3];
        }
        Iridium_SAT_62: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[3];
        }
        Iridium_SAT_63: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[3];
        }
        Iridium_SAT_64: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[3];
        }
        Iridium_SAT_65: SatComm {
            parameters:
                @display("i=device/satellite_vl");
            gates:
                ethg[3];
        }
	connections:
		Iridium_SAT_0.ethg[0] <--> Iridium_SAT_1.ethg[0]
		Iridium_SAT_0.ethg[1] <--> Iridium_SAT_11.ethg[0]
		Iridium_SAT_1.ethg[1] <--> Iridium_SAT_2.ethg[0]
		Iridium_SAT_1.ethg[2] <--> Iridium_SAT_12.ethg[0]
		Iridium_SAT_2.ethg[1] <--> Iridium_SAT_3.ethg[0]
		Iridium_SAT_2.ethg[2] <--> Iridium_SAT_13.ethg[0]
		Iridium_SAT_3.ethg[1] <--> Iridium_SAT_4.ethg[0]
		Iridium_SAT_3.ethg[2] <--> Iridium_SAT_14.ethg[0]
		Iridium_SAT_4.ethg[1] <--> Iridium_SAT_5.ethg[0]
		Iridium_SAT_4.ethg[2] <--> Iridium_SAT_15.ethg[0]
		Iridium_SAT_5.ethg[1] <--> Iridium_SAT_6.ethg[0]
		Iridium_SAT_5.ethg[2] <--> Iridium_SAT_16.ethg[0]
		Iridium_SAT_6.ethg[1] <--> Iridium_SAT_7.ethg[0]
		Iridium_SAT_6.ethg[2] <--> Iridium_SAT_17.ethg[0]
		Iridium_SAT_7.ethg[1] <--> Iridium_SAT_8.ethg[0]
		Iridium_SAT_7.ethg[2] <--> Iridium_SAT_18.ethg[0]
		Iridium_SAT_8.ethg[1] <--> Iridium_SAT_9.ethg[0]
		Iridium_SAT_8.ethg[2] <--> Iridium_SAT_19.ethg[0]
		Iridium_SAT_9.ethg[1] <--> Iridium_SAT_10.ethg[0]
		Iridium_SAT_9.ethg[2] <--> Iridium_SAT_20.ethg[0]
		Iridium_SAT_10.ethg[1] <--> Iridium_SAT_0.ethg[2]
		Iridium_SAT_10.ethg[2] <--> Iridium_SAT_21.ethg[0]
		Iridium_SAT_11.ethg[1] <--> Iridium_SAT_12.ethg[1]
		Iridium_SAT_11.ethg[2] <--> Iridium_SAT_22.ethg[0]
		Iridium_SAT_12.ethg[2] <--> Iridium_SAT_13.ethg[1]
		Iridium_SAT_12.ethg[3] <--> Iridium_SAT_23.ethg[0]
		Iridium_SAT_13.ethg[2] <--> Iridium_SAT_14.ethg[1]
		Iridium_SAT_13.ethg[3] <--> Iridium_SAT_24.ethg[0]
		Iridium_SAT_14.ethg[2] <--> Iridium_SAT_15.ethg[1]
		Iridium_SAT_14.ethg[3] <--> Iridium_SAT_25.ethg[0]
		Iridium_SAT_15.ethg[2] <--> Iridium_SAT_16.ethg[1]
		Iridium_SAT_15.ethg[3] <--> Iridium_SAT_26.ethg[0]
		Iridium_SAT_16.ethg[2] <--> Iridium_SAT_17.ethg[1]
		Iridium_SAT_16.ethg[3] <--> Iridium_SAT_27.ethg[0]
		Iridium_SAT_17.ethg[2] <--> Iridium_SAT_18.ethg[1]
		Iridium_SAT_17.ethg[3] <--> Iridium_SAT_28.ethg[0]
		Iridium_SAT_18.ethg[2] <--> Iridium_SAT_19.ethg[1]
		Iridium_SAT_18.ethg[3] <--> Iridium_SAT_29.ethg[0]
		Iridium_SAT_19.ethg[2] <--> Iridium_SAT_20.ethg[1]
		Iridium_SAT_19.ethg[3] <--> Iridium_SAT_30.ethg[0]
		Iridium_SAT_20.ethg[2] <--> Iridium_SAT_21.ethg[1]
		Iridium_SAT_20.ethg[3] <--> Iridium_SAT_31.ethg[0]
		Iridium_SAT_21.ethg[2] <--> Iridium_SAT_11.ethg[3]
		Iridium_SAT_21.ethg[3] <--> Iridium_SAT_32.ethg[0]
		Iridium_SAT_22.ethg[1] <--> Iridium_SAT_23.ethg[1]
		Iridium_SAT_22.ethg[2] <--> Iridium_SAT_33.ethg[0]
		Iridium_SAT_23.ethg[2] <--> Iridium_SAT_24.ethg[1]
		Iridium_SAT_23.ethg[3] <--> Iridium_SAT_34.ethg[0]
		Iridium_SAT_24.ethg[2] <--> Iridium_SAT_25.ethg[1]
		Iridium_SAT_24.ethg[3] <--> Iridium_SAT_35.ethg[0]
		Iridium_SAT_25.ethg[2] <--> Iridium_SAT_26.ethg[1]
		Iridium_SAT_25.ethg[3] <--> Iridium_SAT_36.ethg[0]
		Iridium_SAT_26.ethg[2] <--> Iridium_SAT_27.ethg[1]
		Iridium_SAT_26.ethg[3] <--> Iridium_SAT_37.ethg[0]
		Iridium_SAT_27.ethg[2] <--> Iridium_SAT_28.ethg[1]
		Iridium_SAT_27.ethg[3] <--> Iridium_SAT_38.ethg[0]
		Iridium_SAT_28.ethg[2] <--> Iridium_SAT_29.ethg[1]
		Iridium_SAT_28.ethg[3] <--> Iridium_SAT_39.ethg[0]
		Iridium_SAT_29.ethg[2] <--> Iridium_SAT_30.ethg[1]
		Iridium_SAT_29.ethg[3] <--> Iridium_SAT_40.ethg[0]
		Iridium_SAT_30.ethg[2] <--> Iridium_SAT_31.ethg[1]
		Iridium_SAT_30.ethg[3] <--> Iridium_SAT_41.ethg[0]
		Iridium_SAT_31.ethg[2] <--> Iridium_SAT_32.ethg[1]
		Iridium_SAT_31.ethg[3] <--> Iridium_SAT_42.ethg[0]
		Iridium_SAT_32.ethg[2] <--> Iridium_SAT_22.ethg[3]
		Iridium_SAT_32.ethg[3] <--> Iridium_SAT_43.ethg[0]
		Iridium_SAT_33.ethg[1] <--> Iridium_SAT_34.ethg[1]
		Iridium_SAT_33.ethg[2] <--> Iridium_SAT_44.ethg[0]
		Iridium_SAT_34.ethg[2] <--> Iridium_SAT_35.ethg[1]
		Iridium_SAT_34.ethg[3] <--> Iridium_SAT_45.ethg[0]
		Iridium_SAT_35.ethg[2] <--> Iridium_SAT_36.ethg[1]
		Iridium_SAT_35.ethg[3] <--> Iridium_SAT_46.ethg[0]
		Iridium_SAT_36.ethg[2] <--> Iridium_SAT_37.ethg[1]
		Iridium_SAT_36.ethg[3] <--> Iridium_SAT_47.ethg[0]
		Iridium_SAT_37.ethg[2] <--> Iridium_SAT_38.ethg[1]
		Iridium_SAT_37.ethg[3] <--> Iridium_SAT_48.ethg[0]
		Iridium_SAT_38.ethg[2] <--> Iridium_SAT_39.ethg[1]
		Iridium_SAT_38.ethg[3] <--> Iridium_SAT_49.ethg[0]
		Iridium_SAT_39.ethg[2] <--> Iridium_SAT_40.ethg[1]
		Iridium_SAT_39.ethg[3] <--> Iridium_SAT_50.ethg[0]
		Iridium_SAT_40.ethg[2] <--> Iridium_SAT_41.ethg[1]
		Iridium_SAT_40.ethg[3] <--> Iridium_SAT_51.ethg[0]
		Iridium_SAT_41.ethg[2] <--> Iridium_SAT_42.ethg[1]
		Iridium_SAT_41.ethg[3] <--> Iridium_SAT_52.ethg[0]
		Iridium_SAT_42.ethg[2] <--> Iridium_SAT_43.ethg[1]
		Iridium_SAT_42.ethg[3] <--> Iridium_SAT_53.ethg[0]
		Iridium_SAT_43.ethg[2] <--> Iridium_SAT_33.ethg[3]
		Iridium_SAT_43.ethg[3] <--> Iridium_SAT_54.ethg[0]
		Iridium_SAT_44.ethg[1] <--> Iridium_SAT_45.ethg[1]
		Iridium_SAT_44.ethg[2] <--> Iridium_SAT_55.ethg[0]
		Iridium_SAT_45.ethg[2] <--> Iridium_SAT_46.ethg[1]
		Iridium_SAT_45.ethg[3] <--> Iridium_SAT_56.ethg[0]
		Iridium_SAT_46.ethg[2] <--> Iridium_SAT_47.ethg[1]
		Iridium_SAT_46.ethg[3] <--> Iridium_SAT_57.ethg[0]
		Iridium_SAT_47.ethg[2] <--> Iridium_SAT_48.ethg[1]
		Iridium_SAT_47.ethg[3] <--> Iridium_SAT_58.ethg[0]
		Iridium_SAT_48.ethg[2] <--> Iridium_SAT_49.ethg[1]
		Iridium_SAT_48.ethg[3] <--> Iridium_SAT_59.ethg[0]
		Iridium_SAT_49.ethg[2] <--> Iridium_SAT_50.ethg[1]
		Iridium_SAT_49.ethg[3] <--> Iridium_SAT_60.ethg[0]
		Iridium_SAT_50.ethg[2] <--> Iridium_SAT_51.ethg[1]
		Iridium_SAT_50.ethg[3] <--> Iridium_SAT_61.ethg[0]
		Iridium_SAT_51.ethg[2] <--> Iridium_SAT_52.ethg[1]
		Iridium_SAT_51.ethg[3] <--> Iridium_SAT_62.ethg[0]
		Iridium_SAT_52.ethg[2] <--> Iridium_SAT_53.ethg[1]
		Iridium_SAT_52.ethg[3] <--> Iridium_SAT_63.ethg[0]
		Iridium_SAT_53.ethg[2] <--> Iridium_SAT_54.ethg[1]
		Iridium_SAT_53.ethg[3] <--> Iridium_SAT_64.ethg[0]
		Iridium_SAT_54.ethg[2] <--> Iridium_SAT_44.ethg[3]
		Iridium_SAT_54.ethg[3] <--> Iridium_SAT_65.ethg[0]
		Iridium_SAT_55.ethg[1] <--> Iridium_SAT_56.ethg[1]
		Iridium_SAT_56.ethg[2] <--> Iridium_SAT_57.ethg[1]
		Iridium_SAT_57.ethg[2] <--> Iridium_SAT_58.ethg[1]
		Iridium_SAT_58.ethg[2] <--> Iridium_SAT_59.ethg[1]
		Iridium_SAT_59.ethg[2] <--> Iridium_SAT_60.ethg[1]
		Iridium_SAT_60.ethg[2] <--> Iridium_SAT_61.ethg[1]
		Iridium_SAT_61.ethg[2] <--> Iridium_SAT_62.ethg[1]
		Iridium_SAT_62.ethg[2] <--> Iridium_SAT_63.ethg[1]
		Iridium_SAT_63.ethg[2] <--> Iridium_SAT_64.ethg[1]
		Iridium_SAT_64.ethg[2] <--> Iridium_SAT_65.ethg[1]
		Iridium_SAT_65.ethg[2] <--> Iridium_SAT_55.ethg[2]
}