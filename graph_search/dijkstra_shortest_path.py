# Import graph class
from graph_utility import create_graph_from_txt_file, Graph


def min_next_distance(graph, processed_vertexes, distances, chain):
    min_distance = float("inf")
    w_star = ''  # initialize w-star

    # grab the first processed node
    for processed_v in processed_vertexes:
        # Look at each connection of the processed node
        for x in graph.get_vertex(processed_v).get_connections():
            # find id of the connection
            z = x.get_id()
            # if the node is not processed then investigate it
            if z not in processed_vertexes:
                # greedy criterian should be the sum of distances from s to v + length(v-w)
                if min_distance > (graph.get_vertex(processed_v).get_weight(x) + distances[processed_v]):
                    min_distance = (graph.get_vertex(processed_v).get_weight(x) + distances[processed_v])
                    w_star = z

                    # if w_star == 92:
                    #     print('processed_v is: ', processed_v, 'test: ', chain_step, ' w star is: ', w_star)

    # print('min_dist: ', min_distance, ' w_star: ', w_star, ' prev_dist: ', distances[processed_v])

    # chain[w_star] = chain[chain_step].add(w_star)
    return min_distance, w_star





def dijkstra_shortest_path(graph, inital_element):
    processed_vertexes = set()
    unprocessed_vertexes = set()
    distances = {}
    chain = {}

    # update unprocessed-vertexes set
    for x in graph.get_vertices():
        unprocessed_vertexes.add(x)

    # update data objects for inital element
    processed_vertexes.add(inital_element)
    distances[inital_element] = 0
    chain[inital_element] = [inital_element]
    unprocessed_vertexes.remove(inital_element)

    # check if there is an unprocessed vertex
    while unprocessed_vertexes != set():
        min_distance, w_star = min_next_distance(graph, processed_vertexes, distances, chain)

        # w star is a list.. so we need to grab the element
        if w_star != '':
            unprocessed_vertexes.remove(w_star)
            processed_vertexes.add(w_star)
            distances[w_star] = min_distance
        else:
            # print(processed_vertexes)
            # print(unprocessed_vertexes)
            # print("hm, no new nodes to connect to")
            break

    # print(chain[152])
    print(distances[152])





graph = create_graph_from_txt_file('/Users/talmadgefarringer/Downloads/dijkstraData.txt')
dijkstra_shortest_path(graph, 1)
# print()
# graph.get_vertex(1).get_connections()

# g = Graph()
#
# g.add_vertex(0)
# g.add_vertex(1)
# g.add_vertex(2)
# g.add_vertex(6)
# g.add_vertex(7)
# g.add_vertex(8)
#
# g.add_edge(0, 1, 4)
# g.add_edge(1, 2, 8)
# g.add_edge(0, 7, 8)
# g.add_edge(7, 8, 7)
# g.add_edge(7, 6, 1)
#
# dijkstra_shortest_path(g, 0, 8)
