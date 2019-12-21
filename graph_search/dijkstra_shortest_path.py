# Import graph class
from graph_utility import create_graph_from_txt_file


def min_next_distance(graph, processed_vertexes, unprocessed_vertexes, distances):
    min_distance = 100000000000000
    w_star = ['z'] # initialize w-star

    # grab the first unprocessed node
    for processed_v in processed_vertexes:
        # Look at each connection of the processed node
        for x in graph.get_vertex(processed_v).get_connections:
            # if the node isnt processed then investigate it
            if x not in processed_vertexes:
                if min_distance > (graph.get_vertex(processed_v).get_weight + distances[processed_v]):
                    min_distance = (graph.get_vertex(processed_v).get_weight + distances[processed_v])
                    w_star.pop()
                    w_star.append(x)

    return min_distance, w_star





def dijkstra_shortest_path(graph, inital_element, ultimate_element):
    processed_vertexes = set()
    unprocessed_vertexes = set()
    distances = {}

    # update data objects for inital element
    processed_vertexes.add(inital_element)
    distances[inital_element] = 0

    # update unprocessed-vertexes set
    for x in graph.get_vertices():
        unprocessed_vertexes.add(x)

    while ultimate_element not in processed_vertexes:
        min_distance, w_star = min_next_distance(graph, processed_vertexes, unprocessed_vertexes, distances)

        # w star is a list.. so we need to grab the element
        w_star_entry = w_star.pop()
        unprocessed_vertexes.remove(w_star_entry)
        processed_vertexes.add(w_star_entry)
        distances[w_star_entry] = min_distance




# node 1 has 0 connections.. ?
graph = create_graph_from_txt_file('/Users/talmadgefarringer/Downloads/dijkstraData.txt')
# dijkstra_shortest_path(graph, 1, 7)
graph.get_vertex(1).get_connections()