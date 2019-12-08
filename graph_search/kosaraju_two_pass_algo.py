from __future__ import absolute_import
from collections import defaultdict

# # Import graph class
from depth_first_search import graph


def reverse_graph(graph_to_reverse: dict) -> dict:
    '''
    This function reverses all the edges in a graph.  Required for step 1 of this algo.
    :param graph_to_reverse:
    '''
    reversed_graph = graph()

    for k in graph_to_reverse.graph:
        for v in graph_to_reverse.graph[k]:
            reversed_graph.addEdge(v, k)

    return reversed_graph

def DFS_loop(graph):
    # reverse the graph
    g_reverse = reverse_graph(graph)

    # Mark all the vertices as not visited
    visited = dict()
    finish_time_dict = dict()
    finish_order_list = []
    leader_dict = defaultdict(list)

    for x in g_reverse.return_all_nodes():
        visited[x] = False

    for x in g_reverse.return_all_nodes():
        if not visited[x]:
            g_reverse.DFS_search(x, visited, finish_time_dict, finish_order_list)

    print(visited)
    # print(finish_time_dict)

    # reset the visited dict to False
    for x in g_reverse.return_all_nodes():
        visited[x] = False


    # leaders -- vertex from which DFS was called that first discovered that node
    # loop 9 -> 1 (based on finishing time)
    print('finish time dict is: ', finish_time_dict)

    for x in reversed(range(0, len(finish_time_dict))):
        if not visited[finish_time_dict[x]]:

            graph.DFS_search(finish_time_dict[x], visited, finish_time_dict, finish_order_list)

            for k, v in visited.items():
                if v:
                    leader_dict[x].append(k)


    print(visited)
    print(leader_dict)



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

    # run DFS loop
    DFS_loop(g)

if __name__ == "__main__":
    # execute only if run as a script
    main()

