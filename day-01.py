
from timeit import Timer
def is_bianweici(word1,word2):
    if len(word1) != len(word2):
        return False
    # 统计字符串出现的次数
    word1_dict = {}
    for i in range(0,len(word1)):
        if word1[i] not in word1_dict:
            word1_dict[word1[i]] = 1
        else:
            word1_dict[word1[i]] += 1
    
    word2_dict = {}
    for i in range(0,len(word2)):
        if word2[i] not in word2_dict:
            word2_dict[word2[i]] = 1
        else:
            word2_dict[word2[i]] += 1
    if len(word1_dict.keys()) != len(word2_dict.keys()):
        return False

    # 比较key和value是否都相等
    for (key,value) in word1_dict.items():
        if key not in word2_dict:
            return False
        else:
            if value != word2_dict[key]:
                return False
    return True

def test():
    x = list(range(0,2000000))
    
    x1 = Timer("x.pop()","from __main__ import x")
    x2 = Timer("x.pop(0)","from __main__ import x")

    print("x1=={}".format(x1.timeit(1000)))
    print("x2=={}".format(x2.timeit(1000)))

from dataStruct import Stack
# 栈的应用，括号匹配
def isBanlance(word):

    qoutoes = Stack()

    for i in range(0,len(word)):

        if word[i] == "(":
            # 如果是左括号就加入到栈顶
            qoutoes.push(word[i])
        else:
            # 如果是右边的括号要看栈是否为空
            if qoutoes.isEmpty():
                print("栈为空")
                return False
            else:
                qoutoes.pop()
    if qoutoes.isEmpty():
        return True
    else:
        return False
# 栈的应用，进制转换，算法：除以进制数取余，然后逆序输出就得到结果
def covertToTwo(num):
    stack = Stack()
    while num > 0 :
        reminder = int(num % 2)
        stack.push(reminder)
        num = int(num / 2)
    
    ret = ""
    while not stack.isEmpty():
        ret += str(stack.pop())
    print(ret)


# 栈的应用：中缀表达式转换为后缀表达式
# 算法：从左往右遍历字符，遇到数字就输出，遇到符号就入栈，入栈前要和栈顶的符号进行优先级判断，
# 如果栈顶优先级高就出栈，直到栈顶的优先小于当前符号
def midExpressionToSuffixExpression(mid):
    nums = "0123456789"
    priorityDict = {}
    priorityDict["*"] = 3
    priorityDict["/"] = 3
    priorityDict["+"] = 2
    priorityDict["-"] = 2
    priorityDict["("] = 1
    # 初始化空栈和输出数组
    stack = Stack()
    outputs = []

    for i in mid:
        if i in nums:
            outputs.append(i)
        elif i == "(":
            stack.push(i)
        elif i == ")":
            stackTop = stack.pop()
            while stackTop != "(":
                outputs.append(stackTop)
                stackTop = stack.pop()
        else:
            # 保证栈顶的优先级最高
            while (not stack.isEmpty()) and (priorityDict[stack.peek()] >= priorityDict[i]):
                outputs.append(stack.pop())
            stack.push(i)
    
    while not stack.isEmpty():
        outputs.append(stack.pop())

    return "".join(outputs)


# 栈的应用
def calculateSuffixExpression(suffixE):
    stack = Stack()
    nums = "0123456789"
    for i in suffixE:
        if i in nums:
            stack.push(i)
        else:
            # 计算符号
            rightNum = stack.pop()
            leftNum = stack.pop()
            if i == '+':
                ret = int(leftNum) + int(rightNum)
                stack.push(ret)
            elif i == "-":
                ret = int(leftNum) - int(rightNum)
                stack.push(ret)
            elif i == "*":
                ret = int(leftNum) * int(rightNum)
                stack.push(ret)
            else:
                ret = int(leftNum) / int(rightNum)
                stack.push(ret)
    while not stack.isEmpty():
        print(stack.pop())






if __name__ == '__main__':
    
    # print("test")
    # print(isBanlance("(())"))

    # print(isBanlance("(()"))

    # covertToTwo(8)

    # ret = midExpressionToSuffixExpression("1+2-3*4+5/6-7")
    # print(ret)
    calculateSuffixExpression("12+34*-56/+7-")


