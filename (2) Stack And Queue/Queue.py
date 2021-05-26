class Queue:
    def __init__(self):
        self.queue=[]

    def enqueue(self,data):
        self.queue.append(data)

    def isempty(self):
        return self.queue!=[]

    def dequeue(self):
        if self.isempty():
            return self.queue.pop(0)
        else:
            print("The Queue Is Empty (Underflow)")

    def peek(self):
        return self.queue[-1]

    def display(self):
        print(self.queue)

obj=Queue()
print("Calling The enqueue Function")
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
print("\nDisplaying The Queue")
obj.display()
print("\nCalling The dequeue Function")
print("dequeued Item :",obj.dequeue())
print("dequeued Item :",obj.dequeue())
print("dequeued Item :",obj.dequeue())
print("\nDisplaying The List After dequeue Function")
obj.display()
print("dequeued Item :",obj.dequeue())
print("\nTrying to use dequeue function when the queue is empty")
obj.dequeue()