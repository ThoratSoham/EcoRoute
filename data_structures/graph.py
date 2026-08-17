class Graph:
    def __init__(self):
        self.adjacency = {}
        self.nodes={}

    def add_node(self,node_id, name, lat, lng):
        if node_id not in self.nodes:
            self.nodes[node_id] = {"name":name,"lat":lat, "lng":lng}
            self.adjacency[node_id] = []

    def add_edges(self, from_id, to_id, distance_km, traffic_factor, mode):
        self.adjacency[from_id].append({
            "to":to_id, "distance":distance_km,
            "traffic_factor":traffic_factor,
            "mode":mode
        })

        self.adjacency[to_id].append({
            "to":from_id, "distance":distance_km,
            "traffic_factor":traffic_factor,
            "mode":mode
        })

    def get_neighbors(self, node_id):
        return self.adjacency.get(node_id,[])

    def get_all_nodes(self):
        return self.nodes

    def to_dict(self):
        edges = []
        seen = set()
        for from_id, neighbors in self.adjacency.items():
            for edge in neighbors:
                key = tuple(sorted([from_id, edige["to"]])) + (edge[mode],)
                if key in seen:
                    continue
                seen.add(key)
                edges.append({
                    "from":from_id,
                    "to":edge["to"],
                    "distance":edge["distance"],
                    "traffic_factor":edge["traffic_factor"],
                    "mode":edge["mode"]
                })
        return {"nodes":self.nodes,"edges":edges}
    