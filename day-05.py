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

    

if __name__ == "__main__":
    # print(sum([1,2,3]))

    # drawFiveRect()
    # drawSpiral(200)
    # time.sleep(200)

    t.left(90)
    tree(15)
    time.sleep(10)