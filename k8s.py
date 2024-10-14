from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom

graph_attr = {
    "layout":"dot",
    "compound":"true",
}

with Diagram("", filename="k8s", show=False, graph_attr=graph_attr, direction="TB"):
    with Cluster("K8s"):
        with Cluster("1", graph_attr={"label": "", "style": "invisible"}):
            with Cluster("monitoring"):
                monitoring = [
                    Custom("Prometheus", "./resources/prometheus.png"),
                    Custom("Grafana", "./resources/grafana.png"),
                    Custom("Loki", "./resources/loki.png"),
                ]

            with Cluster("downloaders"):
                downloaders = [
                    Custom("qBitTorrent", "./resources/qBitTorrent.png"),
                    Custom("sabnzbd", "./resources/sab.png"),
                    Custom("MullvadVPN", "./resources/mullvad.png"),
                ]

            with Cluster("arr"):
                arr = [
                    Custom("Radarr", "./resources/radarr.png"),
                    Custom("Sonarr", "./resources/sonarr.png"),
                    Custom("Prowlarr", "./resources/prowlarr.png"),
                ]

        with Cluster("2", graph_attr={"label": "", "style": "invisible"}):
            with Cluster("media"):
                media = [
                    Custom("Jellyfin", "./resources/jellyfin.svg"),
                ]

            with Cluster("postgres"):
                postgres = [
                    Custom("PostgreSQL", "./resources/postgresql.svg"),
                ]

            with Cluster("redis"):
                redis = [
                    Custom("Redis", "./resources/redis.svg"),
                ]
                
            with Cluster("cloud"):
                cloud = [
                    Custom("Nextcloud", "./resources/nextcloud.svg"),
                    Custom("", "./resources/immich.svg"),
                ]

        with Cluster("3", graph_attr={"label": "", "style": "invisible"}):
            with Cluster("firefly"):
                firefly = [
                    Custom("Firefly III", "./resources/fireflyiii.png"),
                    #Custom("", "./resources/wallos.png")
                ]

            with Cluster("wiki"):
                wiki = [
                    Custom("WikiJS", "./resources/wikijs.png"),
                ]

            with Cluster("diet"):
                diet = [
                    Custom("Mealie", "./resources/mealie.png"),
                    Custom("Tandoor", "./resources/tandoor.svg"),
                ]

            with Cluster("kanban"):
                kanban = [
                    Custom("Focalboard", "./resources/focalboard.svg"),
                    Custom("Planka", "./resources/planka.png"),
                ]
            
        monitoring[0] >> Edge(lhead="cluster_2", style="invis") >> media[0]
        media[0] >> Edge(lhead="cluster_3", style="invis") >> firefly[0]
