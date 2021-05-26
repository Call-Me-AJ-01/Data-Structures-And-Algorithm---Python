# Note: There is a Bug In This Program
# if we insert more than 10 items the program goes for infinite loop

class HashTable:
    def __init__(self):
        self.capacity=10
        self.keys=[None]*self.capacity
        self.values=[None]*self.capacity

    def key_generator(self,key):
        sum_=0
        for i in key:
            sum_+=ord(i)
        return sum_%self.capacity

    def insert(self,key,data):
        index=self.key_generator(key)
        while self.keys[index] is not None:
            if self.keys[index]==key:
                self.values[index]=data
                return
            index=(index+1)%self.capacity

        self.keys[index]=key
        self.values[index]=data

    def get_value(self,key):
        index=self.key_generator(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                print(self.values[index])
                return self.values[index]
            index=(index+1)%self.capacity
        else:
            print('The Given Key is Not Present In The Dictionary')

obj=HashTable()
obj.insert('adhavan',22)
obj.insert('adam1',31)

obj.get_value('adam8')

