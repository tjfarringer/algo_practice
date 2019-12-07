from __future__ import absolute_import

# # Import graph class
from depth_first_search import graph


def reverse_graph(graph_to_reverse: dict) -> dict:
    '''
    This function reverses all the edges in a graph.  Required for step 1 of this algo.
    :param graph:
    '''
    reversed_graph = graph()

    for k in graph_to_reverse.graph:
        for v in graph_to_reverse.graph[k]:
            reversed_graph.addEdge(v, k)

    return reversed_graph

def DFS_loop(graph):
    # Mark all the vertices as not visited
    visited = dict()
    finish_time_dict = dict()
    finish_order_list = []

    for x in graph.return_all_nodes():
        visited[x] = False

    for x in graph.return_all_nodes():
        if visited[x] == False:
            graph.DFS_search(x, visited, finish_time_dict, finish_order_list)

    print(visited)
    print(finish_time_dict)
    magical_order = finish_time_dict


    current_parent_node =


def main():
    # creating a test graph
    g = graph()
    g.addEdge(7, 1)
    g.addEdge(4, 7)
    g.addEdge(1, 4)
    g.addEdge(9, 7)
    g.addEdge(6, 9)
    g.addEdge(3, 6)
    g.addEdge(9, 3)
    g.addEdge(8, 6)
    g.addEdge(2, 8)
    g.addEdge(5, 2)
    g.addEdge(8, 5)

    # reverse the graph
    g_reverse = reverse_graph(g)

    DFS_loop(g_reverse)

if __name__ == "__main__":
    # execute only if run as a script
    main()

