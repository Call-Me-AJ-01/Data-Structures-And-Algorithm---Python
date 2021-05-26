# Note : BFS goes layer by layer approach

class Node:
    def __init__(self,data):
        self.name=data
        self.visited=False
        self.adjacency_list=[]

def BFS(data):
    queue=[data]
    while queue:
        actual_node = queue.pop(0)
        actual_node.visited = True
        print(actual_node.name)
        for item in actual_node.adjacency_list:
            if item.visited is not True:
                queue.append(item)

# creating Nodes
node1=Node('A')
node2=Node('B')
node3=Node('C')
node4=Node('D')
node5=Node('E')

# creating a connection between nodes
node1.adjacency_list.append(node2)
node1.adjacency_list.append(node3)
node2.adjacency_list.append(node4)
node2.adjacency_list.append(node5)

# Calling The Function
BFS(node1)