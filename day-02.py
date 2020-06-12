from dataStruct import Queue
# 约瑟夫问题，n个人玩游戏，报数到m出列，最后剩下谁
def yuesefuGame(names,num):
    queue = Queue()
    for name in names:
        queue.enqueue(name)
    
    while queue.size() > 1 :
        for i in range(num):
            queue.enqueue(queue.dequeeu())
        queue.dequeeu()
    return queue.dequeeu()

"""
一个实验室内：在任何给定的一个小时内，实验室里都约有10个学生。他们在这一个小时内最多打印2次，并且打印的页数从1到20不等。实验室内只有1台打印机且比较老旧，每分钟只能以低质量打印10页，或者提高质量打印5页。降低打印速度可能导致学生等待时间过长，这里计算学生平均需要等待多长时间才能拿到打印好的文章。

说明：

学生打印的文章可能有1-20页，如果各页数出现的概率相等，那么实际打印任务的时长可以通过1-20的一个随机数来模拟。
如果实验室里有10个学生，并且在一个小时内，每个人都打印两次，那么平均每小时就有20个打印任务，相当于每180秒1个任务，故可以通过1-180的一个随机数来模拟每秒内产生打印任务的概率。如果随机数正好是180，那么久认为有一个打印任务被创建。
主要模拟步骤 ：
（1）创建一个打印任务队列。每一个人物到来时都会有一个时间戳。一开始，队列是空的。
（2） 针对每一秒(currentsecond) ，执行以下操作：

 是否有新创建的打印任务？如果是，以currentsecond作为其时间戳并将该任务加入到队列中。

 如果打印机空闲，并且有正在等待执行的任务，执行以下操作：

从队列中取出第一个任务并提交给打印机；

用currentsecond减去该任务的时间戳，以此计算等待时间；

将该任务的等待时间存入一个列表，以后备用；

根据该任务的页数，计算执行时间

 打印机进行一秒的打印，同时从该任务的执行时间中减去一秒。

 如果打印任务执行完毕，或者说任务需要的时间减为0，则说明打印机回到空闲状态。

（3）当模拟完成之后，根据等待时间列表中的值计算平均等待时间。
"""
import random
class Task:
    def __init__(self,createTime):
        self.createTime = createTime
        self.pages = random.randrange(1,21)
    
    def getPages(self):
        return self.pages
    def getCreateTime(self):
        return self.createTime
    def waitTime(self,currentTime):
        return currentTime - self.createTime

class Printer:
    def __init__(self,pages):
        # 每分钟打印的页数
        self.printPage = pages
        self.currentTask = None
        # 打印剩下时间
        self.timeLeft = 0

    def isBusy(self):
        if self.currentTask != None:
            return True
        else:
            return False
    # 打印倒计时
    def tick(self):
        if self.currentTask != None:
            self.timeLeft = self.timeLeft - 1
            if self.timeLeft == 0:
                self.currentTask = None
    # 开始任务
    def startTask(self,task):
        self.currentTask = task
        self.timeLeft = task.getPages()*60/self.printPage

def simulation(seconds,printPanges):
    printer = Printer(printPanges)
    printQueue = Queue()
    waitTimes = []
    for currentScond in range(seconds):
        # 生成任务
        if random.randrange(1,181) == 180:
            task = Task(currentScond)
            printQueue.enqueue(task)

        # 如果打印处于空闲状态而且队列部位空就取出队首执行任务
        if (not printer.isBusy()) and (not printQueue.isEmpty()):
            newTask = printQueue.dequeeu()
            waitTimes.append(newTask.waitTime(currentScond))
            printer.startTask(newTask)
        # 打印任务倒计时
        printer.tick()
    
    averageWaitTime = sum(waitTimes)/ len(waitTimes)
    print("averageWaitTime = {} ****** taskLeft = {}".format(averageWaitTime,printQueue.size()))






if __name__ == "__main__":
    # ret = yuesefuGame(["1","2","3","4","5","6"],7)
    # print("11")
    for i in range(10):
        simulation(3600,10)

