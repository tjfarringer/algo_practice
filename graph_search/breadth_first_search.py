
# defaultdict means that if a key is not found in the dictionary, then instead of a KeyError being thrown, a new entry is created
# need to use a type with the defaultdict
from collections import defaultdict

# Create a queue class, which we will use to determine which node to explore
class Queue():
    '''
    Obviously we could have used the core python queue class
    '''

    def __init__(self, initial_list=[]):
        self.queue = list(initial_list)

    def add_to_queue(self, item):
        self.queue.append(item)

    def next_element(self):
        if len(self.queue) < 1:
            None
        else:
            return self.queue.pop(0)

    def display_queue(self):
        return self.queue

    def length_of_queue(self):
        return len(self.queue)


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

    def addEdge(self, u, v):
        '''
        Add edge from u to v
        :param u:
        :param v:
        :return:
        '''
        self.graph[u].append(v)

    def BFS_search(self, node, visited: dict, queue: Queue):
        '''
        Do a breadth-first search starting with the node provided. Visited is a dictionary that informs us
         if the node has been visited in the past.

        :param node:  Node to start the search from
        :param visited:  Dictionary showing if a node has already been visited
        :return:
        '''

        print('length of queue: ', queue.length_of_queue())
        while queue.length_of_queue() > 0:
            # grab next node to explore
            v = queue.next_element()
            # set current node to be explored
            visited[v] = True

            print('Currently exploring: ', v)

            for next_node in self.graph[v]:
                if visited[next_node] == False:
                    queue.add_to_queue(next_node)
                    # set it to explored at this stage, otherwise you could add a node to the queue several times
                    visited[next_node] = True


    def BFS(self, node):
        '''
        Main driver
        '''
        # Mark all the vertices as not visited
        # create visited as a dictionary
        visited = dict()

        # Need to loop through the keys and values because a node might not have a unique edge
        for k in g.return_keys():
            visited[k] = False

        for v in g.return_values():
            # if a node has multiple connections -- that will be a list
            # need to parse through the list
            if type(v) == list:
                for x in v:
                    visited[x] = False
            else:
                visited[v] = False

        # create our queue class
        bfs_queue = Queue()
        # add the initial node to the queue
        bfs_queue.add_to_queue(node)

        # Call the BFS function
        self.BFS_search(node, visited, bfs_queue)


# creating a test graph + searching through it
g = graph()
g.addEdge('s', 'a')
g.addEdge('s', 'b')
g.addEdge('a', 'c')
g.addEdge('b', 'c')
g.addEdge('b', 'd')
g.addEdge('c', 'd')
g.addEdge('c', 'e')
g.addEdge('d', 'e')


print("Following is BFS from (starting from vertex 2)")
g.BFS('s')