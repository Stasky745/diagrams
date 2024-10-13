from diagrams import Diagram, Cluster, Edge
from diagrams.generic.network import Router, Switch, Firewall
from diagrams.generic.os import Windows
from diagrams.generic.storage import Storage
from diagrams.custom import Custom

graph_attr = {
    "layout":"dot",
    "compound":"true",
}

with Diagram("", filename="home_networking", show=False, graph_attr=graph_attr, direction="TB"):
    switch = Switch("Switch")

    with Cluster("10", graph_attr={"label": "VLAN10: TRUSTED\n192.168.10.0/24"}):
        void = Custom("192.168.10.4", "./resources/void.png")
        vlan10 = [
            void,
            Custom("WorkLaptop", "./resources/macbook.png"),
            Custom("Trusted WiFi", "./resources/ap_unifi.png")
        ]
    
    with Cluster("42", graph_attr={"label": "VLAN42: SERVERS\n192.168.42.0/24"}):

        with Cluster("K8s"):
            k8s = [
                Custom("\n192.168.42.10", "./resources/talos.svg"),
                Custom("\n192.168.42.11", "./resources/talos.svg"),
                Custom("\n192.168.42.12", "./resources/talos.svg"),
            ]
        
        nas = Storage("NAS/DAS")

        vlan42 = [
            k8s,
            nas,
            Windows("Sunshine/\nMoonlight")
        ]
    
    
    with Cluster("50", graph_attr={"label": "VLAN50: GUEST\n192.168.50.0/24"}):
        vlan50 = [
            Custom("Guest WiFi", "./resources/ap_unifi.png"),
        ]

    with Cluster("70", graph_attr={"label": "VLAN70: IOT\n192.168.70.0/24"}):
        vlan70 = [
            Custom("FireTV", "./resources/firetv.png")
        ]
    
    with Cluster("90", graph_attr={"label": "VLAN90: CCTV\n192.168.90.0/24"}):
        vlan90 = [
            Custom("CCTV", "./resources/cctv.png")
        ]
    
    with Cluster("100", graph_attr={"label": "VLAN100: VPN\n192.168.100.0/24"}):
        vlan100 = [
            Custom("WireGuard", "./resources/wireguard.svg")
        ]

    Router("ISP") >> Firewall("VyOS") >> switch

    switch >> Edge(lhead="cluster_10") >> vlan10[len(vlan10)//2]
    switch >> Edge(lhead="cluster_42") >> vlan42[len(vlan42)//2]
    switch >> Edge(lhead="cluster_50") >> vlan50[len(vlan50)//2]
    switch >> Edge(lhead="cluster_70") >> vlan70[len(vlan70)//2]
    switch >> Edge(lhead="cluster_90") >> vlan90[len(vlan90)//2]
    switch >> Edge(lhead="cluster_100") >> vlan100[len(vlan100)//2]

