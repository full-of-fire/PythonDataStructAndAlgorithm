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


# 这里使用链表实现无序列表
class Node:
    def __init__(self,item):
        self.item = item
        self.next = None
    
    def setNext(self,node):
        self.next = node
    
    def getNext(self):
        return self.next

    def getItem(self):
        return self.item

class UnSortedList:
    def __init__(self):
        self.head = None

    def addItem(self,item):
        if self.head is None:
            self.head = Node(item)
        else:
            node = Node(item)
            head = self.head
            self.head = node
            node.setNext(head)
    def removeItem(self,item):
        if self.head != None and item == self.head.getItem():
            # 如果删除的数据项为第一个,直接以移动head指针
            self.head = self.head.getNext()
        else:
            # 如果不是第一个，就遍历
            next = self.head.getNext()
            preciousNode = self.head
            while next != None:
                if next.getItem() == item:
                    preciousNode.next = next.getNext()
                preciousNode = next
                next = next.getNext()
    def size(self):
        if self.head is Node:
            return 0
        else:
            count = 0 
            next = self.head
            while next is not None:
                count += 1
                next = next.getNext()
            return count

    def isEmpty(self):
        return self.size() == 0

    def searchItem(self,item):
        if self.head is None:
            return False
        else:
            next = self.head
            isContain = False
            while next is not None and (isContain == False):
                if next.getItem() == item:
                    isContain = True
                next = next.getNext()
            return isContain

    def appendItem(self,item):
        if self.head is None:
            self.head = Node(item)
        else:
            next = self.head
            while next is not None:
                if next.getNext() is None:
                    next.setNext(Node(item))
                    break
                next = next.getNext()
    
    def printAll(self):
        next = self.head
        while next is not None:
            print(next.getItem())
            next = next.getNext()
                


        


        