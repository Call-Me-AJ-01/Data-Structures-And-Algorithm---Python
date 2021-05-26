# linked list(singly)

# Topics Covered:-
'''
    *creating of linklist
    *inseting element to linklist
    *displaying elements of the linklist
    *inserting element before head node
    *inserting element after a given data'''

# short note on linked list(how to create a link list)

###Note:-
# create a class for each single node(in my case i have give class "Node")
# create another class and attach all the nodes to the list
# (in my case i have given class "Linkedlist")
'''
note: the first node is called as head node and the last node is called as tail node

            --------------------------------------------------------
            |                                                      |
            |  ------------       ------------       ------------  |
            |  |    |      |      |    |      |      |    |      | |
            |  |Data|Addr ------> |Data|Addr  ------>|Data|None  | |
   |---------->|    |      |      |    |      |      |    |      | |
   |        |  ------------       ------------       ------------  |
   |        |       |                                              |
   |        |       |->Node class(single node)                     |
   |        |                                                      |  
   |        |                                                      |
   |        -------------------------------------------------------
   |                                |
   |                                |->Linked list class(group of nodes "(single node)" together)
   |                                                  |
step 1:-                                              |
create a class for single node'''  # |


# |
class Node:  # creating class for single node           #|
    def __init__(self, data):  # |
        self.data = data  # |
        self.next = None  # |
        # |


'''step 2:-  <-----------------------------------------                                           
create another class to link all the single nodes'''


class Linkedlist:  # creating class to link all the single nodes
    def __init__(self):  # first time the linkedlist head node must be None this construct is called only once when the obj is created for linked list
        self.head = None

    def insert(self, data):
        obj = Node(data)  # creating obj for class Node and sending value to the class Node
        if self.head == None:
            self.head = obj
            return
        last_node = self.head
        while last_node.next != None:
            last_node = last_node.next
        last_node.next = obj  # linking the single node to the main class "Linkedlist"

    def display(self):
        current_node = self.head
        while current_node != None:
            print(current_node.data)
            current_node = current_node.next

    def inserting_on_first_place(self, data):
        seperate_node = Node(data)
        seperate_node.next = self.head  # here the value is inserted before head
        self.head = seperate_node  # since the value is inserted first(before head node) we have to point that node as a head node

    def inserting_after_the_given_data(self, prev_data, data):
        current_node = self.head
        if not prev_data:  # this checks whether the given previous data is available or not
            print("not available")
        else:
            while current_node.data != prev_data:
                current_node = current_node.next
            obj = Node(data)
            obj.next = current_node.next
            current_node.next = obj

    def remove(self,data):
        if self.head.data==data:
            self.head=self.head.next
        else:
            current_node = self.head
            while current_node.next is not None and current_node.next.data!=data:
                current_node=current_node.next
            if current_node.next is None:
                print('The Given Data Is Not Available On The Linked List\n')
                return
            del_node=current_node.next
            current_node.next=del_node.next
            print('Deleted ',del_node.data)


lobj = Linkedlist()

# inserting data to list
lobj.insert(1)
lobj.insert(2)
lobj.insert(3)
lobj.insert(4)

print("before calling inserting_on_first_place function\n")

# displaying datas from linked list
lobj.display()
print("\nafter calling inserting_on_first_place function\n")

# inserting data before head node
lobj.inserting_on_first_place(10)
print("\nafter inserting 10\n")
lobj.display()
lobj.inserting_on_first_place(20)
print("\nafter inserting 20\n")
lobj.display()
lobj.inserting_on_first_place(30)
print("\nafter inserting 30\n")
lobj.display()

# inserting given data after the given prev data
print("\ninserting data after the given data Example:-\n")
lobj.inserting_after_the_given_data(3, 10)  # (prev_data,data_to be added) u can get both the data as input also
print("\nafter inserting \n")
lobj.display()

#deleting The given data
print("Before Deleting The Data\n")
lobj.display()
print("After Deleting The Data\n")
lobj.remove(10)
lobj.display()
