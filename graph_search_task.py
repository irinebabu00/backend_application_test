# ##################################################
# 1) Load workpiece graph and feature graph data from  json file
# ##################################################

import json
import networkx as nx
from networkx.algorithms import isomorphism

# Note: Available files are: workpiece_graph.json, feature_graph.json

# TODO
with open("workpiece_graph.json", "r") as wpfile:
    workpiece_graph = json.load(wpfile)
with open("feature_graph.json", "r") as fgfile:
    feature_graph = json.load(fgfile)

# ##################################################
# 2) Create graphs from loaded data
# ##################################################

# Hint: The library networkx helps you to create a graph. You can use the nx.Graph() class to create a graph.
# Note: Other appraoches are also possible.

# TODO
def construct_graph(graph_data):
    G = nx.Graph()
    for node, attrs in graph_data["nodes"]:
        node_id, node_attrs = node, attrs
        G.add_node(node_id, **node_attrs)
    for edge in graph_data["edges"]:
        node1, node2, edge_attrs = edge
        G.add_edge(node1, node2, **edge_attrs)
    return G
workpiece_graph_new = construct_graph(workpiece_graph)
feature_graph_new = construct_graph(feature_graph)

# Note: Optional task - Visualize the graph
# Example code:
# from pyvis.network import Network
# nt = Network()
# nt.from_nx(workpiece_graph)
# nt.show("graph.html", notebook=False)

# ##################################################
# 3) Check if the feature graph is a subgraph of the workpiece workpiece and find any other matching subgraphs
# ##################################################


# TODO

# ##################################################
# 4) Results
# ##################################################

# Print results if matches are found. Return the number of matches and the node ids.

# TODO
