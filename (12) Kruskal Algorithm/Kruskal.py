# Representation Of Nodes(Vertex) in graph
class Vertex:
    def __init__(self, name):
        self.name = name
        self.node = None


# Representation Of Nodes in Tree Format
class Node:
    def __init__(self, node_rank, node_id, node_parent=None):
        self.node_id = node_id
        self.rank = node_rank
        self.parent = node_parent


class Edge:
    def __init__(self, weight, start_node, end_node):
        self.start_node = start_node
        self.end_node = end_node
        self.weight = weight

    def __lt__(self, other_edge):
        return self.weight < other_edge.weight


class Disjointset:
    def __init__(self, vertex_list):
        self.vertex_list = vertex_list
        self.root_node = []
        self.make_set()

    def find(self, node):
        current_node = node
        while current_node.parent is not None:
            current_node = current_node.parent

        root = current_node
        current_node = node

        while current_node is not root:
            temp = current_node.parent
            current_node.parent = root
            current_node = temp

        return root.node_id

    def merge(self, node1, node2):
        index1 = self.find(node1)
        index2 = self.find(node2)

        if index1 == index2:
            return
        else:
            root1 = self.root_node[index1]
            root2 = self.root_node[index2]
            if root1.rank < root2.rank:
                root1.parent = root2
            elif root1.rank > root2.rank:
                root2.parent = root1
            else:
                root1.parent = root2
                root1.rank += 1

    def make_set(self):
        for v in self.vertex_list:
            node = Node(0, len(self.root_node))
            v.node = node
            self.root_node.append(node)


class Kruskal:
    def __init__(self, vertex_list, edge_list):
        self.vertex_list = vertex_list
        self.edge_list = edge_list

    def shortest_path(self):
        disjpintset = Disjointset(self.vertex_list)
        min_span_tree = []

        self.edge_list.sort()

        for edge in self.edge_list:
            start = edge.start_node
            end = edge.end_node

            if disjpintset.find(start.node) is not disjpintset.find(end.node):
                min_span_tree.append(edge)
                disjpintset.merge(start.node, end.node)

        for edge in min_span_tree:
            print(edge.start_node.name, '-', edge.end_node.name, '-', edge.weight)


if __name__ == '__main__':
    # vertices in the G(V,E)
    vertex1 = Vertex("A")
    vertex2 = Vertex("B")
    vertex3 = Vertex("C")
    vertex4 = Vertex("D")
    vertex5 = Vertex("E")
    vertex6 = Vertex("F")
    vertex7 = Vertex("G")

    # edges
    edge1 = Edge(2, vertex1, vertex2)
    edge2 = Edge(6, vertex1, vertex3)
    edge3 = Edge(5, vertex1, vertex5)
    edge4 = Edge(10, vertex1, vertex6)
    edge5 = Edge(3, vertex2, vertex4)
    edge6 = Edge(3, vertex2, vertex5)
    edge7 = Edge(1, vertex3, vertex4)
    edge8 = Edge(2, vertex3, vertex6)
    edge9 = Edge(4, vertex4, vertex5)
    edge10 = Edge(5, vertex4, vertex7)
    edge11 = Edge(5, vertex6, vertex7)

    # have to create a list out of these edges and vertices
    vertices = [vertex1, vertex2, vertex3, vertex4, vertex5, vertex6, vertex7]
    edges = [edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10, edge11]

    # let's run the algorithm
    algorithm = Kruskal(vertices, edges)
    algorithm.shortest_path()
