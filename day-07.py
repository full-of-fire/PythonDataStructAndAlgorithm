

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

# 插入排序：
# 核心思想：将列表分为有序列表和无序列表，每次从无序列表中取出一个元素和已经排序的列表进行对比
# 找到其合适的位置然后交换
# 由于移动元素仅包含一次赋值操作，所以其性能较好
# 怎么优化？：越有序比对的次数就越少
def insertSort(nums):
    for index in range(1,len(nums)):   
        currentValue = nums[index]
        positon = index - 1
        # 从后往前遍历对比,如果发现元素比他大就往后移动一位
        while positon >=0 and nums[positon] > currentValue:
            nums[positon+1] = nums[positon]
            positon -= 1
        nums[positon+1] = currentValue


# 思想：将序列分为多个子序列，然后分别进行插入排序
# 其时间复杂度在O(n)~O(n2)之间
def shellSort(nums):
    gap = len(nums) // 2

    while gap > 0 :
        print(gap)
        for cur in range(gap,len(nums)):
            i = cur
            while i >= gap and nums[i-gap] > nums[i]:
                nums[i - gap], nums[i] = nums[i], nums[i-gap]
                i -= gap
        gap = gap // 2

# 归并排序：先将数组进行拆分，直到只有一个元素，就当已经排序好了，然后对排序结果进行合并
def mergeSort(nums):
    if len(nums) == 1:
        return nums
    midIndex = int(len(nums) / 2)

    left = mergeSort(nums[:midIndex])
    right = mergeSort(nums[midIndex:])

    # 合并
    i = 0 
    j = 0
    results = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            results.append(left[i])
            i += 1
        else:
            results.append(right[j])
            j += 1
    
    results.extend(left[i:])
    results.extend(right[j:])
    return results



    


if __name__ == "__main__":

    nums = [19,13,11,5,4,3,2]
    # bubbleSort(nums)
    # advanceBubbleSort(nums)
    # selectionSort(nums)
    # insertSort(nums)
    # shellSort(nums)
    ret = mergeSort(nums)
    print(ret)
    print(nums)