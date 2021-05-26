class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class Doubly_Linked:
    def __init__(self):
        self.head=None
        self.prev=None
        self.next=None

    def insert(self,data):
        if self.head is None:
            new=Node(data)
            self.head=new
            self.last_node=self.head
            return
        new=Node(data)
        self.last_node.next=new
        new.prev=self.last_node
        self.last_node=new

    def display(self):
        self.current_node=self.head
        while self.current_node is not None:
            print(self.current_node.data,end=' ')
            self.current_node=self.current_node.next

    def print_from_left_to_right(self):
        print('\nPrinting From Left to Right Format (correct Order)')
        self.current_node=self.head
        while self.current_node is not None:
            print(self.current_node.data,end=' ')
            self.current_node=self.current_node.next

    def print_from_right_to_left(self):
        print('\nPrinting from Right to Left Format (Reverse Order)')
        self.current_node=self.last_node
        while self.current_node is not None:
            print(self.current_node.data,end=' ')
            self.current_node=self.current_node.prev

    def insert_on_first_position(self,data):
        new=Node(data)
        new.next=self.head
        self.head.prev=new
        self.head=new

    def inserting_element_after_a_given_data(self,prev,data):
        new=Node(data)
        self.current_node=self.head
        while self.current_node.data!=prev:
            self.current_node=self.current_node.next
        new.next=self.current_node.next
        new.prev=self.current_node
        self.current_node.next=new
        self.current_node=new.next
        self.current_node.prev=new

dobj=Doubly_Linked()
print('Inserting Element In The list')
dobj.insert(1)
dobj.insert(2)
dobj.insert(3)
dobj.insert(4)
dobj.insert(5)
dobj.insert(6)
print('After Inserting Element In The list')
dobj.display()
dobj.print_from_left_to_right()
dobj.print_from_right_to_left()
print('\nInserting Element in the front')
dobj.insert_on_first_position(100)
dobj.insert_on_first_position(200)
dobj.insert_on_first_position(300)
dobj.insert_on_first_position(400)
dobj.display()
print('\nBefore Inserting Element In The Give Data')
dobj.display()
print('\nAfter Inserting Element In The Give Data')
dobj.inserting_element_after_a_given_data(4,'->inserted after "4"<-')
dobj.display()