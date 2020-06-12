class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)

class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeeu(self):
        return self.items.pop()
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)

#  双端队列
class Dqueue:
    def __init__(self):
        self.items = []
    
    def addFront(self,item):
        self.items.insert(0,item)
    def removeFront(self):
        return self.items.pop(0)
    
    def addRear(self,item):
        self.items.append(item)
    def removeRear(self):
        return self.items.pop()
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)

        