import sys
print(sys.path)

# # Import graph class
from .depth_first_search import graph

# creating a test graph + searching through it
g = graph()
g.addEdge(1, 7)
g.addEdge(7, 4)
g.addEdge(4, 1)
g.addEdge(7, 9)
g.addEdge(9, 6)
g.addEdge(6, 3)
g.addEdge(3, 9)
g.addEdge(6, 8)
g.addEdge(8, 2)
g.addEdge(2, 5)
g.addEdge(5, 8)


