# Note:
#
# -> Left heavy situation:
# if the  balance calculator value is gretater than 1 then it is a left heavy situation
#     there are two types of left heavy situation
#         -> if the balance calculator value of the left child of the node is "less than 0" then it is a 'left right' heavy situation
#         -> else it is a left left heavy situation
#
# -> Right heavy situation:
# if the balance calculator value is lesser than -1 then it is a roght heavy situation
#     there are two types of right heavy situation
#         -> if the balance calculator value of the right child of the node is "greater than 0" then it is a 'right left' heavy situation
#         ->else it is a right right heavy situation

class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.parent = parent
        self.height = 0


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_all(data, self.root)

    def insert_all(self, data, node):
        if data < node.data:
            if node.left_child is None:
                node.left_child = Node(data, node)
                self.height = max(self.get_height(node.left_child), self.get_height(node.right_child)) + 1
            else:
                self.insert_all(data, node.left_child)
        else:
            if node.right_child is None:
                node.right_child = Node(data, node)
                self.height = max(self.get_height(node.left_child), self.get_height(node.right_child)) + 1
            else:
                self.insert_all(data, node.right_child)

        self.handle_violation(node)

    def remove(self, data):
        if self.root is None:
            print('The tree is empty cannot delete the given data :', data)
        else:
            self.remove_node(data, self.root)

    def remove_node(self, data, node):
        if data < node.data:
            self.remove_node(data, node.left_child)
        elif data > node.data:
            self.remove_node(data, node.right_child)
        else:
            if node.left_child is None and node.right_child is None:
                print('removing The Leaf node :', data)
                if node.parent is None:
                    self.root = None
                else:
                    if node.parent.left_child is not None and node.parent.left_child.data is data:
                        node.parent.left_child = None
                    else:
                        node.parent.right_child = None
                self.handle_violation(node.parent)

            elif node.left_child is None and node.right_child is not None:
                print('removing the node with single right child :', data)
                if node.parent is None:
                    self.root = node.right_child
                else:
                    if node.parent.left_child is not None and node.parent.left_child.data is data:
                        node.parent.left_child = node.right_child
                    else:
                        node.parent.right_child = node.right_child
                self.handle_violation(node.parent)

            elif node.right_child is None and node.left_child is not None:
                print('removing the node with single left child :', data)
                if node.parent is None:
                    self.root = node.left_child
                else:
                    if node.parent.left_child is not None and node.parent.left_child.data is data:
                        node.parent.left_child = node.left_child
                    else:
                        node.parent.right_child = node.left_child
                self.handle_violation(node.parent)

            else:
                print('removing the node with two child :', data)
                get_max_from_left_sub_tree = self.get_max(node.left_child)
                node.data = get_max_from_left_sub_tree.data
                print('Node value changed to :', node.data)
                self.remove_node(get_max_from_left_sub_tree.data, get_max_from_left_sub_tree)

    def get_max(self, node):
        if node.right_child is not None:
            return self.get_max(node.right_child)
        return node

    def get_height(self, node):
        if node is None:
            return -1
        return node.height

    def calculate_balance(self, node):
        if node is None:
            return 0
        return self.get_height(node.left_child) - self.get_height(node.right_child)

    def handle_violation(self, node):
        while node is not None:
            self.violation_helper(node)
            node = node.parent

    def violation_helper(self, node):
        balance_val = self.calculate_balance(node)

        if balance_val > 1:  # Left heavy situation
            if self.calculate_balance(node.left_child) < 0:  # Left Right Heavy Situation
                self.rotate_left(node.left_child)
            self.rotate_right(node)

        if balance_val < -1:  # Right heavy situation
            if self.calculate_balance(node.right_child) > 0:  # Right Left Heavy Situation
                self.rotate_right(node.right_child)
            self.rotate_left(node)

    def rotate_right(self, node):
        print("Rotating to the right on node ", node.data)

        temp_left_node = node.left_node
        t = temp_left_node.right_node

        temp_left_node.right_node = node
        node.left_node = t

        if t is not None:
            t.parent = node

        temp_parent = node.parent
        node.parent = temp_left_node
        temp_left_node.parent = temp_parent

        if temp_left_node.parent is not None and temp_left_node.parent.left_node == node:
            temp_left_node.parent.left_node = temp_left_node

        if temp_left_node.parent is not None and temp_left_node.parent.right_node == node:
            temp_left_node.parent.right_node = temp_left_node

        if node == self.root:
            self.root = temp_left_node

        node.height = max(self.get_height(node.left_node), self.get_height(node.right_node)) + 1
        temp_left_node.height = max(self.get_height(temp_left_node.left_node),
                                    self.get_height(temp_left_node.right_node)) + 1

    def rotate_left(self, node):
        print("Rotating to the left on node ", node.data)

        temp_right_node = node.right_node
        t = temp_right_node.left_node

        temp_right_node.left_node = node
        node.right_node = t

        if t is not None:
            t.parent = node

        temp_parent = node.parent
        node.parent = temp_right_node
        temp_right_node.parent = temp_parent

        if temp_right_node.parent is not None and temp_right_node.parent.left_node == node:
            temp_right_node.parent.left_node = temp_right_node

        if temp_right_node.parent is not None and temp_right_node.parent.right_node == node:
            temp_right_node.parent.right_node = temp_right_node

        if node == self.root:
            self.root = temp_right_node

        node.height = max(self.get_height(node.left_node), self.get_height(node.right_node)) + 1
        temp_right_node.height = max(self.get_height(temp_right_node.left_node),
                                     self.get_height(temp_right_node.right_node)) + 1

    def traverse(self):
        if self.root is not None:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node):
        if node.left_child:
            self.traverse_in_order(node.left_child)

        l = ''
        r = ''
        p = ''

        if node.left_child is not None:
            l = node.left_child.data
        else:
            l = 'NULL'

        if node.right_child is not None:
            r = node.right_child.data
        else:
            r = 'NULL'

        if node.parent is not None:
            p = node.parent.data
        else:
            p = 'NULL'

        print("%s left: %s right: %s parent: %s height: %s" % (node.data, l, r, p, node.height))

        if node.right_child:
            self.traverse_in_order(node.right_child)

if __name__ == '__main__':
    avl = AVLTree()
    avl.insert(5)
    avl.insert(3)
    avl.insert(6)
    avl.insert(1)

    avl.remove(6)
    avl.traverse()
