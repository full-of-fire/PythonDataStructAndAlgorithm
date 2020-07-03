

# 冒泡排序：
# 核心思想：通过n-1躺对比，通过对比交换直到排序完成
# 优势：不占用额外的存储空间
def bubbleSort(nums):
    for passNum in range(len(nums)-1,0,-1):
        print(passNum)
        for i in range(passNum):
            if nums[i] > nums[i+1]:
                tmp = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = tmp
# 冒泡排序的优化：如果发现有一趟，没有进行交换就证明排序已经完成了
def advanceBubbleSort(nums):
    passNum = len(nums) - 1
    exchangeNum = True

    while passNum > 0 and exchangeNum:
        exchangeNum = False
        for i in range(passNum):
            if nums[i] > nums[i+1]:
                exchangeNum = True
                tmp = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = tmp
        passNum = passNum - 1

#选择排序也是在冒泡排序上面进行优化，每次对比后不交换元素，只记录最大元素位置，减少交换次数
def selectionSort(nums):

    for passNum in range(len(nums) - 1,0,-1):
        maxNumIndex = 0
        for i in range(1,passNum+1):
            if nums[i] > nums[maxNumIndex]:
                maxNumIndex = i
        # 进行交换
        tmp = nums[maxNumIndex]
        nums[maxNumIndex] = nums[passNum]
        nums[passNum] = tmp

    


if __name__ == "__main__":

    nums = [19,13,11,5,4,3,2]
    # bubbleSort(nums)
    # advanceBubbleSort(nums)
    selectionSort(nums)
    print(nums)