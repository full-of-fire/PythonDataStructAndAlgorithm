# 数的应用，表达式的解析
from dataStruct import BinaryTree
from dataStruct import Stack
# ((5-3)*(8-2))
def expressionTree(expression=''):
    stack = Stack()
    emptyTree = BinaryTree("")
    stack.push(emptyTree)
    currentNode  = emptyTree
    for item in expression:
        if item == '(':
            # 创建左边节点，当前节点下降，就是入栈保存起来
            print("创建左字树节点")
            currentNode.insertLeftChild("")
            stack.push(currentNode)
            currentNode = currentNode.getLeftChild()
        elif item not in ['+','-','*','/',')']:
            print("遇到数字{}给当前节点赋值，并且返回其父节点".format(item))
            currentNode.setRootValue(item)
            currentNode = stack.pop()
            print(currentNode.getLeftChild().getRootValue())
        elif item in ['+','-','*','/']:
            print("遇到操作符号 == {}，需要创建一个空右边字树".format(item))
            currentNode.setRootValue(item)
            print(currentNode.getRootValue())
            currentNode.insertRight("")
            stack.push(currentNode)
            currentNode = currentNode.getRightChild()
        elif item == ')':
            currentNode = stack.pop()
    return emptyTree

# 前序遍历            
def priciousTree(tree):
    if tree is None:
        return
    print(tree.getRootValue())
    priciousTree(tree.getLeftChild())
    priciousTree(tree.getRightChild())
# 后序遍历
def postOrder(tree):
    if tree is None:
        return
    postOrder(tree.getLeftChild())
    postOrder(tree.getRightChild())
    print(tree.getRootValue())
# 中序遍历
def inOrder(tree):
    if tree is None:
        return 
    inOrder(tree.getLeftChild())
    print(tree.getRootValue())
    inOrder(tree.getRightChild())

def calculateTree(tree):
    if tree.getLeftChild() is None and tree.getRightChild() is None:
        return tree.getRootValue()
    else:
        leftResult = int(calculateTree(tree.getLeftChild()))
        rightResult = int(calculateTree(tree.getRightChild()))
        root =  tree.getRootValue()
        if root in ['+','-','*','/']:
            if root == '+':
                return leftResult + rightResult
            elif root == '-':
                return leftResult - rightResult
            elif root == '*':
                return leftResult * rightResult
            else:
                return leftResult / rightResult






if __name__ == "__main__":
    
    ret = expressionTree("((5-3)*4)")
    # priciousTree(ret)
    # inOrder(ret)
    # priciousTree(ret)
    print(calculateTree(ret))
