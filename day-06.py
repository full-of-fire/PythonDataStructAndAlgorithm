

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


if __name__ == "__main__":

    nums = [1,3,5,7,9]
    print(searchUnSortList(nums,6))