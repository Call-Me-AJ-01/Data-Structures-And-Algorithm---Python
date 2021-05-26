# Note : DFS goes branch by branch approach

class Node:
    def __init__(self,data):
        self.name=data
        self.adjacency_list=[]
        self.visited=False

def DFS(data):
    stack=[data]

    while stack:
        actual_node=stack.pop(-1)
        actual_node.visited=True
        print(actual_node.name)
        for item in actual_node.adjacency_list:
            if item.visited is not True:
                stack.append(item)

# creating Node
node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')
node5 = Node('E')

# creating Link Between The Nodes
node1.adjacency_list.append(node3)
node1.adjacency_list.append(node2)
node2.adjacency_list.append(node4)
node2.adjacency_list.append(node5)

# calling the functiom
DFS(node1)