# 回文词的检测
from dataStruct import Dqueue
def isHuiwen(text):
    dqueue = Dqueue()
    for i in text:
        dqueue.addRear(i)
    
    stillEqual = True
    while dqueue.size() > 1 and stillEqual:
        frontWord = dqueue.removeFront()
        rearWord = dqueue.removeRear()
        if frontWord != rearWord:
            stillEqual = False
    return stillEqual


if __name__ == "__main__":
    print(isHuiwen("上海自来水来自海上"))

    print(isHuiwen("abcdcb"))
