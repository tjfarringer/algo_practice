from __future__ import absolute_import
from collections import defaultdict

# # Import graph class
from graph_utility import Graph, create_graph_from_txt_file


def dijkstra_shortest_path(graph, inital_element):
    processed_vertex = set()
    distances = {}

    # update data objects for inital element
    processed_vertex.add(inital_element)
    distances[inital_element] = 0

    # while processed_vertex != graph.return_all_nodes():

graph_utility.create_graph_from_txt_file('/Users/talmadgefarringer/Downloads/dijkstraData.txt')