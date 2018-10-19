# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
# 输入：一个 递增 排序的数组的旋转；
# 输出：旋转数组的最小元素
# 例如：[3,4,5,1,2] 为 [1,2,3,4,5]的一个旋转，该数组的最小值为1

# -*- coding:utf-8 -*-
# 思路一：直接用 python 自带的 min 函数 
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        n = len(rotateArray)
        if n==0:
            return 0
        if rotateArray is None:
            return
        else:
            return min(rotateArray)

# 思路一是最直观的解法，但是这种思路没有利用旋转数组的特性；不难注意到旋转
# 之后的数组可以分为两个排序的子数组，而且前面子数组的元素都大于或等于后面子
# 数组的元素。我们还注意到最小的元素刚好是这两个子数组的分界线。之前我们提到
# 在排序的数组中可以用二分法查找实现 O(logn) 的查找。因此我们可以使用二分
# 查找的思路来寻找这个最小的元素。
# 分析过程
# array = [3,4,5,1,2]
# n = len(array)
# startIndex = 0
# endIndex = n - 1

# start = 3
# end = 2
# mid = 5
# mid > start 
# start_index = mid_index
# start = 5
# end = 2
# mid = 1
# end_index = mid_index
# start_index-end_index = 1
# return end_index

# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        n = len(rotateArray)
        if n == 0:
            return 0
        # 若数组长度为1或者数组在旋转之后仍然是递增数列
        elif n == 1 or rotateArray[0]<rotateArray[n-1]:
            return rotateArray[0]
        else:
            startIndex = 0
            endIndex = n - 1
            midIndex = (startIndex + endIndex)/2
            if rotateArray[startIndex] == rotateArray[endIndex] == rotateArray[midIndex]:
                return min(rotateArray) # 若三个指针指向的数字都相同，则依然选择用顺序查找
            while (rotateArray[startIndex] > rotateArray[endIndex]):
                if (rotateArray[startIndex] <= rotateArray[midIndex]):
                    startIndex = midIndex
                elif (rotateArray[midIndex] <= rotateArray[endIndex]):
                    endIndex = midIndex
                midIndex = (startIndex + endIndex)/2
                if (endIndex - startIndex == 1):
                    return rotateArray[endIndex]

print(Solution().minNumberInRotateArray([3,4,5,1,2]))

