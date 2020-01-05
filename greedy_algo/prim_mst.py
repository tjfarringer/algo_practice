# Import graph class
from graph_search.graph_utility import create_graph_from_txt_file, Graph


# assumptions
# take in a graph with all nodes connected in some way
# each edge cost is distinct

g = Graph()

g.add_vertex(0)
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)

g.add_edge(0, 1, 1)
g.add_edge(1, 2, 4)
g.add_edge(2, 3, 5)
g.add_edge(3, 0, 2)
g.add_edge(1, 3, 3)




def prim_mst(g: Graph):
    # this is the set of all vertices from the initalization graph
    all_vertices = set()
    # x is the set of vertices we've visited
    mst_vertices = set()
    # This is our MST tree
    t = Graph()

    # update total-vertexes set
    for vertex in g.get_vertices():
        all_vertices.add(vertex)

    while all_vertices != mst_vertices:
        pass

        # Let e = (u, v) be the cheapest edge of G with u in mst_vertices and v not in mst_vertices
        # add e to t
        # add v to mst_vertices
