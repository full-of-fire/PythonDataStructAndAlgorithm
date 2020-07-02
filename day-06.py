

# 无序列表的搜索
# 算法分析：
# 1.如果不在列表中，最好和最坏的强开都是n词比对
# 2.如果在列表中，最好的情况是1次，最坏的情况是n词，平均n/2
def searchUnSortList(unSortList,item):

    found = False
    index = 0
    while index < len(unSortList) and not found:
        if unSortList[index] == item:
            found = True
        else:
            index = index + 1
    return found

# 有序列表的搜索
# 算法分析：
# 1.如果在列表中：最好的情况是1次，最坏的情况是n次
# 2.如果不在列表中：最好的情况1次，最坏的情况是n次
def searSortList(sortList,item):
    found = False
    index = 0
    inList = True
    while index < len(sortList) and not found and inList:
        if sortList[index] == item:
            found = True
        else:
            if sortList[index] > item:
                inList = False
            else:
                index = index + 1
    return found

# 顺序表的二分查找
def binarySearch(sortList,item):
    first = 0
    last = len(sortList) - 1
    found = False

    while first <= last and not found:
        midIndex = int((first + last) / 2)
        if sortList[midIndex] == item:
            found = True
        else:
            if sortList[midIndex] > item:
                last = midIndex - 1
            else:
                first = midIndex + 1

    return found
# 二分查找的递归实现：1.最小结束条件，如果是空列表直接返回 2.如何缩小规模 3.调用自身缩小规模
def binarySearchV2(sortList,item):
    midIndex = len(sortList) // 2
    if len(sortList) == 0:
        return False
    elif sortList[midIndex] == item:
        return True
    else:
        if sortList[midIndex] > item:
            return binarySearchV2(sortList[:midIndex],item)
        else:
            return binarySearchV2(sortList[midIndex+1:],item)


if __name__ == "__main__":

    nums = [1,3,5,7,9]
    # print(binarySearch(nums,8))
    print(binarySearchV2(nums,8))