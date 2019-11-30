
# defaultdict means that if a key is not found in the dictionary, then instead of a KeyError being thrown, a new entry is created
# need to use a type with the defaultdict
from collections import defaultdict

# Create a graph class

class graph:

    # constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFS_search(self, node, visited: dict):

        # mark the current node as visited
        visited[node] = True
        print('Just visited: ', node)

        # search for unvisited nodes connected to a previously visited node
        for next_node in self.graph[node]:
            print('Current node: ', node, ' Possible next node: ', next_node)
            if visited[next_node] == False:
                print('Visited: ', next_node)
                # dig into the next node
                self.DFS_search(next_node, visited)

    def DFS(self, node):
        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))

        # Call the recursive helper function
        # to print DFS traversal
        self.DFS_search(node, visited)


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