
# defaultdict means that if a key is not found in the dictionary, then instead of a KeyError being thrown, a new entry is created
# need to use a type with the defaultdict
from collections import defaultdict

# Create a graph class

class graph:

    # constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    def return_keys(self):
        return self.graph.keys()

    def return_values(self):
        return self.graph.values()

    def return_all_nodes(self):
        all_nodes = set()

        for k in graph.return_keys(self):
            all_nodes.add(k)

        for v in graph.return_values(self):
            # if a node has multiple connections -- that will be a list
            # need to parse through the list
            if type(v) == list:
                for x in v:
                    all_nodes.add(x)
            else:
                all_nodes.add(v)

        return all_nodes

    def addEdge(self, u, v):
        '''
        Add edge from u to v
        :param u:
        :param v:
        :return:
        '''
        self.graph[u].append(v)

    def DFS_search(self, node, visited: dict, finish_time_dict: dict, finish_order_list: list):
        '''
        Do a depth-first search starting with the node provided.
        Visited is a dictionary that informs us if the node has been visited in the past.

        :param node:  Node to start the search from
        :param visited:  Dictionary showing if a node has already been visited
        :param finish_time_dict:
        :param finish_order_list:
        :return:
        '''

        # mark the current node as visited
        visited[node] = True
        print('At: ', node)

        # If there is no next node, increment current_finish_time by one and add to the dict
        if len(self.graph[node]) == 0:
            print('at: ', node, ' but no linked objects')
            print('current_finish_time is: ', len(finish_order_list))
            finish_time_dict[len(finish_order_list)] = node
            finish_order_list.append(node)
            print('current_finish_time is: ', len(finish_order_list))

        # search for unvisited nodes connected to a previously visited node
        for next_node in self.graph[node]:
            print('Current node: ', node, ' Possible next node: ', next_node)
            if visited[next_node] == False:
                # print('Visited: ', next_node)
                # dig into the next node
                self.DFS_search(next_node, visited, finish_time_dict, finish_order_list)

                # if that was the last node, increment current_finish_time by one and add to the dict
                if next_node == self.graph[node][len(self.graph[node]) - 1]:
                    print('at: ', node, ' but no unvisited objects - last loop')
                    print('current_finish_time is: ', len(finish_order_list))
                    finish_time_dict[len(finish_order_list)] = node
                    finish_order_list.append(node)
                    print('current_finish_time is: ', len(finish_order_list))

            # if there are no unvisited nodes, increment current_finish_time by one and add to the dict
            elif next_node == self.graph[node][len(self.graph[node])-1]:
                print('at: ', node, ' but no unvisited objects')
                print('current_finish_time is: ', len(finish_order_list))
                finish_time_dict[len(finish_order_list)] = node
                finish_order_list.append(node)
                print('current_finish_time is: ', len(finish_order_list))

    def DFS(self, node):
        '''
        Main driver
        '''
        # Mark all the vertices as not visited
        visited = dict()
        finish_time_dict = dict()
        current_finish_time = 0

        for x in self.return_all_nodes():
            visited[x] = False

        # Call the recursive helper function
        # to print DFS traversal
        self.DFS_search(node, visited, finish_time_dict, current_finish_time)
        print(visited)




def main():
    # creating a test graph + searching through it
    g = graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Following is DFS from (starting from vertex 2)")
    g.DFS(2)


if __name__ == "__main__":
    # execute only if run as a script
    main()