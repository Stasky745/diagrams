from diagrams import Diagram, Cluster, Edge
from diagrams.generic.network import Router, Switch, Firewall
from diagrams.generic.device import Mobile, Tablet
from diagrams.generic.os import Windows
from diagrams.generic.storage import Storage
from diagrams.custom import Custom

graph_attr = {
    "layout":"dot",
    "compound":"true",
}

with Diagram("Home Networking", outformat="svg", show=False, direction="TB", graph_attr=graph_attr):
    switch = Switch("Switch")

    with Cluster("10", graph_attr={"label": "VLAN10 (TRUSTED): 192.168.1.10/24"}):
        void = Custom("PC: 192.168.1.14", "./resources/void.png")
        vlan10 = [
            void,
            Custom("Trusted WiFi", "./resources/ap_unifi.png")
        ]
    
    with Cluster("42", graph_attr={"label": "VLAN42 (SERVERS): 192.168.1.42/24"}):
        talos_m1 = Custom("M1: 192.168.1.45", "./resources/talos.svg")
        talos_m2 = Custom("M2: 192.168.1.46", "./resources/talos.svg")
        talos_m3 = Custom("M3: 192.168.1.47", "./resources/talos.svg")

        nas = Storage("NAS/DAS")

        with Cluster("K8s"):
            k8s = [
                talos_m1,
                talos_m2,
                talos_m3,
            ]
        
        vlan42 = [
            nas,
            Windows("Sunshine/Moonlight")
        ]
    
    
    with Cluster("50", graph_attr={"label": "VLAN50 (GUEST): 192.168.1.50/24"}):
        vlan50 = [
            Mobile(""),
            Tablet(""),
            Custom("Guest WiFi", "./resources/ap_unifi.png")
        ]

    #with Cluster("VLAN70 (IOT): 192.168.1.70/24"):

    Router("ISP") >> Firewall("VyOS") >> switch

    switch >> Edge(lhead="cluster_10") >> vlan10[len(vlan10)//2]
    switch >> Edge(lhead="cluster_42") >> vlan42[len(vlan42)//2]
    switch >> Edge(lhead="cluster_50") >> vlan50[len(vlan50)//2]

    k8s >> nas
