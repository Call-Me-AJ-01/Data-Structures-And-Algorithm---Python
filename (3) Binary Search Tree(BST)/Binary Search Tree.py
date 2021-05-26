class child:
    def __init__(self,data,parent):
        self.data=data
        self.left=None
        self.right=None
        self.parent=parent

class Tree:
    def __init__(self):
        self.head=None

    def insert(self,data):
        if self.head is None:
            self.head=child(data,None)
        else:
            self.insert_node(data,self.head)

    def insert_node(self,data,node):
        if data < node.data:
            if node.left is not None:
                self.insert_node(data,node.left)
            else:
                node.left=child(data,node)
        else:
            if node.right is not None:
                self.insert_node(data,node.right)
            else:
                node.right=child(data,node)

    def print_inorder_traverse(self):
        if self.head is None:
            return 'Head Node is Empty'
        else:
            self.traverse(self.head)

    def traverse(self,node):
        if node.left is not None:
            self.traverse(node.left)

        print(node.data)

        if node.right is not None:
            self.traverse(node.right)

    def remove_node(self,data):
        if self.head is not None:
            self.remove(data,self.head)
        else:
            return 'Head Node is empty(remove_node)'

    def remove(self,data,node):
        if node is None:
            return 'The Tree is Empty'
        else:
            if data < node.data:
                self.remove(data,node.left)
            elif data > node.data:
                self.remove(data,node.right)
            else:
                if node.left is None and node.right is None:
                    print('Deleting The Leaf Node......',node.data)
                    parent=node.parent
                    if parent is not None and parent.left == node:
                        parent.left=None
                    if parent is not None and parent.right == node:
                        parent.right=None
                        
                    if parent is None:
                        self.head=None
                        
                    del node

                elif node.left is not None and node.right is None:
                    print('Deleting The Node with single left child....',node.data)
                    parent=node.parent
                    if parent is not None:
                        if parent.left == node:
                            parent.left=node.left
                        else:
                            parent.right=node.left
                    else:
                        self.head=node.left

                    node.left.parent=parent
                    del node
                    
                elif node.right is not None and node.left is None:
                    print('Deleting Node with a single right child',node.data)
                    parent=node.parent
                    if parent.left == node:
                        parent.left=node.right
                    else:
                        parent.right=node.right

                    node.right.parent=parent
                    del node

                else:
                    print('Deleting Node with two child',node.data)
                    predecessor=self.get_predecessor(node.left)
                    temp=predecessor.data
                    predecessor.data=node.data
                    node.data=temp
                    print(predecessor.data,'is moved to the leaf node')
                    self.remove(data,predecessor)
                    
    def get_predecessor(self,node):
        if node.right is None:
            return node
        self.get_predecessor(node.right)
                          

obj=Tree()
obj.insert(10)
obj.insert(5)
obj.insert(-5)
obj.insert(1)
obj.insert(99)
obj.insert(34)
obj.insert(1000)
obj.print_inorder_traverse()
print()
obj.remove_node(99)
print()
obj.print_inorder_traverse()
