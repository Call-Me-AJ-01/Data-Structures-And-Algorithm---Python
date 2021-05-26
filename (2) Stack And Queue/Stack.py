class Stack:
    def __init__(self):
        self.stack=[]

    def push(self,data):
        self.stack.append(data)

    def isempty(self):
        return self.stack!=[]

    def pop(self):
        if self.isempty():
            return self.stack.pop(-1)
        else:
            print("The Stack Is Empty (Underflow)")

    def peek(self):
        return self.stack[-1]

    def display(self):
        print(self.stack)

obj=Stack()
print("Calling The Push Function")
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
print("\nDisplaying The Stack")
obj.display()
print("\nCalling The Pop Function")
print("Poped Item :",obj.pop())
print("Poped Item :",obj.pop())
print("Poped Item :",obj.pop())
print("\nDisplaying The List After Pop Function")
obj.display()
print("Poped Item :",obj.pop())
print("\nTrying to use pop function when the Stack is empty")
obj.pop()