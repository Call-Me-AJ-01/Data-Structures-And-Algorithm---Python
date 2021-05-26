import sys


class Dijkstra:
    def __init__(self, adjacency_matrix, start_index):
        self.adjacency_matrix = adjacency_matrix
        self.visited = [False for _ in range(len(adjacency_matrix))]
        self.distance = [float('inf') for _ in range(len(adjacency_matrix))]
        self.distance[start_index] = 0

    def get_min_distance(self):
        temp_min_distance = sys.maxsize
        smaller_index = 0
        for index in range(len(self.distance)):
            if self.visited[index] is not True and self.distance[index] < temp_min_distance:
                temp_min_distance = self.distance[index]
                smaller_index = index
        return smaller_index

    def calculate(self):
        for nodes in range(len(self.adjacency_matrix)):
            actual_node = self.get_min_distance()
            print('Considering vertex',actual_node)
            self.visited[actual_node] = True
            for index in range(len(self.adjacency_matrix)):
                if self.adjacency_matrix[actual_node][index] > 0:
                    if self.distance[actual_node] + self.adjacency_matrix[actual_node][index] < self.distance[index]:
                        self.distance[index] = self.distance[actual_node] + self.adjacency_matrix[actual_node][index]

    def print_distances(self):
        print(self.distance)


if __name__ == '__main__':
    m = [[0, 7, 5, 2, 0, 0],
         [7, 0, 0, 0, 3, 8],
         [5, 0, 0, 10, 4, 0],
         [2, 0, 10, 0, 0, 2],
         [0, 3, 4, 0, 0, 6],
         [0, 8, 0, 2, 6, 0]]

    algorithm = Dijkstra(m, 1)
    algorithm.calculate()
    algorithm.print_distances()
