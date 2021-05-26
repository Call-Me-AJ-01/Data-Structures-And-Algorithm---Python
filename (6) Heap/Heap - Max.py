capacity = 10
class Heap: # Note:- This Program is max heap
    def __init__(self):
        self.heap=[0]*capacity
        self.heap_size=0

    def insert(self,data):
        if self.heap==capacity:
            return

        self.heap[self.heap_size]=data
        self.heap_size+=1

        self.move_up(self.heap_size-1)

    def move_up(self,index):
        parent=(index-1)//2

        if index>0 and self.heap[index]>self.heap[parent]: # if the symbol is change to '<' then it is min heap
            self.heap[index],self.heap[parent]=self.heap[parent],self.heap[index]
            self.move_up(parent)

    def get_max(self):
        return self.heap[0]

    def poll(self):
        max_data = self.get_max()
        self.heap[0],self.heap[self.heap_size-1]=self.heap[self.heap_size-1],self.heap[0]
        self.heap_size-=1

        self.move_down(0)
        return max_data

    def move_down(self,index):
        left_child=2*index+1
        right_child=2*index+2
        large_index=index

        if left_child<self.heap_size and self.heap[left_child]>self.heap[index]:
            large_index=left_child
        elif right_child<self.heap_size and self.heap[right_child]>self.heap[large_index]:
            large_index=right_child
        if index!=large_index:
            self.heap[index],self.heap[large_index]=self.heap[large_index],self.heap[index]
            self.move_down(large_index)

    def heap_sort(self):
        for i in range(self.heap_size):
            max_=self.poll()
            print(max_)


obj=Heap()
obj.insert(1)
obj.insert(2)
obj.insert(3)
obj.insert(4)
obj.insert(5)
print(obj.heap) # Printing The Whole Heap Values
obj.heap_sort()
