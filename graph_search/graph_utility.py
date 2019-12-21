
class Vertex():
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

class Graph():
    def __init__(self):
        self.vertex_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vertex_dict.values())

    def add_vertex(self, node):
        self.num_vertices += 1
        new_vertex = Vertex(node)
        self.vertex_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vertex_dict:
            return self.vertex_dict[n]
        else:
            return None

    def add_edge(self, start, end, cost=0):
        if start not in self.vertex_dict:
            self.add_vertex(start)
        if end not in self.vertex_dict:
            self.add_vertex(end)

        self.vertex_dict[start].add_neighbor(self.vertex_dict[end], cost)
        self.vertex_dict[end].add_neighbor(self.vertex_dict[start], cost)

    def get_vertices(self):
        return self.vertex_dict.keys()



def remove_comma(s: str):
    try:
        s = s.replace(',', '')
    except:
        pass

    return s



def create_graph_from_txt_file(txt_file_location):

    graph = Graph()

    f = open(txt_file_location, 'r')
    for line in f:
        split_line = line.split()
        vertex_number = int(split_line[0])

        for edge_tuple in split_line[1:len(split_line) - 1]:
            split_tuple = edge_tuple.split(",")
            vertex = split_tuple[0]
            length = split_tuple[1]
            graph.add_edge(int(vertex_number), int(vertex), int(length))

    # print(graph.get_vertex(1).get_connections())

    return graph