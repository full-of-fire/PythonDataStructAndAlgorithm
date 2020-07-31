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
                


        
# 二叉树
class BinaryTree:
    def __init__ (self,value):
        self.value = value
        self.leftChild = None
        self.rightChild = None
    
    def setRootValue(self,value):
        self.value = value
    
    def getRootValue(self):
        return self.value

    
    def insertLeftChild(self,value):
        if self.leftChild is None:
            # 如果为就新建一个节点进行赋值
            newNode = BinaryTree(value)
            self.leftChild = newNode
        else:
            newNode = BinaryTree(value)
            newNode.leftChild = self.leftChild
            self.leftChild = newNode

    def insertRight(self,value):
        if self.rightChild is None:
            newNode = BinaryTree(value)
            self.rightChild = newNode
        else:
            newNode = BinaryTree(value)
            newNode.rightChild = self.rightChild
            self.rightChild = newNode
    
    def getRightChild(self):
        return self.rightChild
    
    def getLeftChild(self):
        return self.leftChild


# 定义如下：
# Graph() : 创建一个空图
# addVertex(vert) : 将顶点vert加入图中
# addEdge(fromVert, toVert) : 添加有向边
# addEdge(fromVert, toVert, weight):添加带权的有向边
# getVertex(vKey) : 查找名称为vKey的顶点
# getVertices() : 返回图中所有顶点列表
# in : 按照vert in graph的语句形式，返回顶点是否存在图中True/False

# 图的邻接列表的实现
class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
    # 添加一条边
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight
    
    def getConnections(self):
        return self.connectedTo.keys()
    
    def getId(self):
        return self.id
    
    def getWeigth(self,nbr):
        return self.connectedTo[nbr]

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
    
    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None
    
    def __contains__(self,n):
        return n in self.vertList
    
    def addEdge(self,f,to,weight=0):
        if  f not in self.vertList:
            self.addVertex(f)
        if to not in self.vertList:
            self.addVertex(to)
        self.vertList[f].addNeighbor(self.vertList[to],weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())        