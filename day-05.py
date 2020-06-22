# 递归思想的总结：1.结束条件，也就是最小问题，2.如何将大问题分解为相同的小问题

def sum(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        return nums[0] + sum(nums[1:])

import turtle as t
import time

# 画花朵
def drawFlower():
    t.color("red","yellow")
    t.speed(10)
    t.begin_fill

    for _ in range(50):
        t.forward(200)
        t.left(170)
    t.end_fill()
    time.sleep(1)
# 画三角形
def drawTriangle():
    t.forward(200)
    t.left(60)
    t.backward(200)
    t.left(60)
    t.forward(200)
    time.sleep(10)
# 递归应用，任意进制转换：如转换为10进制，如果n小于10就直接查表就能获得其值，大于10就拆分为两个更加小的数据
def convert(n,base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return convert(int(n/base),base) + convertString[n%base]

# 画矩形
def drawRect():
    t.pencolor("red")
    for _ in range(4):
        t.forward(200)
        t.left(90)
    t.done
    time.sleep(5)

def drawFiveRect():

    t.pencolor("red")
    for _ in range(5):
        t.forward(200)
        t.left(144)
    time.sleep(5)

# 画螺旋线
def drawSpiral(linelen):
    if linelen > 0:
        t.forward(linelen)
        t.right(90)
        drawSpiral(linelen - 5)


# 分形树

def tree(lineLen):
    if lineLen > 5:
        # 1.先画主干
        t.forward(lineLen)

        # 2.右树
        t.right(20)
        # 递归调用画右边的小树
        tree(lineLen - 5)
        # 左树
        t.left(40)
        # 递归调用画左树
        tree(lineLen - 5)
        # 回正
        t.right(20)
        t.backward(lineLen)

# 最小硬币数：1.最小问题当找钱直接为硬币数是个数为1 2.如何缩减规模 3.递归调用自身减少规模 4.贪心策略但是效率很低
def minCoins(changes,money):
    # 1.最小问题，如果要找的钱刚刚是硬币的数目就直接返回
    if money in changes:
        return 1
    else:
        # 2.递归调用减少规模
        # 找出最小值
        # minNum = 99999
        for change in [ item for item in changes if item <= money]:
            ret = 1 + minCoins(changes,money - change)
            if ret < minNum:
                minNum =ret
        return minNum
# 如何优化递归调用的解法：消除重复计算问题，采来缓存计算结果， 
def bestMinCoins(coinValueList,change,knowReuslts):
    if change in coinValueList:
        knowReuslts[change] = 1
        return 1
    elif knowReuslts[change] > 1:
        return knowReuslts[change]
    else:
        # 递归调用
        minNum = 99999
        for coin in [ item for item in coinValueList if item <= change]:
            ret = 1 + bestMinCoins(coinValueList,change - coin,knowReuslts)
            if ret < minNum:
                minNum =ret
                knowReuslts[change] = minNum
        return minNum

def testMinCoins():
        # 1.测试最小硬币数
    startTime = time.time()
    ret =  minCoins([5,1,10,25],63)
    endTime = time.time()
    costTime = endTime - startTime
    # time.clock()
    print(ret)
    print("cost time === {}".format(costTime))

def testBestMinCoins():
    startTime = time.time()
    ret =  bestMinCoins([1,5,10,25],63,[0]*64)
    endTime = time.time()
    costTime = endTime - startTime
    # time.clock()
    print(ret)
    print("cost time === {}".format(costTime))


    

if __name__ == "__main__":
    # print(sum([1,2,3]))

    # drawFiveRect()
    # drawSpiral(200)
    # time.sleep(200)

    # t.left(90)
    # tree(15)
    # time.sleep(10)
    # pass
    testBestMinCoins()

