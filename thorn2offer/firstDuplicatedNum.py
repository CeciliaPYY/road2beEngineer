# 题目描述
# 在一个长度为n的数组里的所有数字都在0到n-1的范围内。 
# 数组中某些数字是重复的，但不知道有几个数字是重复的。
# 也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 
# 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。

# 方法一：对列表排序之后，从排序后的数组中找出重复的数字
# -*- coding:utf-8 -*-
class Solution1(object):
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        sortedNumbers = sorted(numbers)
        duplicateRecord = []
        for i in range(1, len(sortedNumbers)-1):
            if sortedNumbers[i-1] == sortedNumbers[i] or sortedNumbers[i] == sortedNumbers[i+1]:
                duplicateRecord.append(sortedNumbers[i])
        if len(duplicateRecord) > 0:
            duplication[0] = duplicateRecord[0]
            return True
        else:
            return False

# -*- coding:utf-8 -*-
class Solution2(object):
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        lookup = {}
        duplicatedNum = []
        for k, v in enumerate(numbers):
            if not v in lookup.values():
                lookup[k] = v
            else:
                duplicatedNum.append(v)
        if len(duplicatedNum) > 0:
            duplication[0] = duplicatedNum[0]
            return True
        else:
            return False

# -*- coding:utf-8 -*-
# 方法三，思路：如果一组数字，其中每个数字都介于 0~n-1 之间，
# 如果这一组数字中不包含重复数字，那么它们的值和下标就会一一对应。
# 如果这组数字中存在重复数字，那么某些位置上就包含不止一个数字，
# 某些位置上不包含数字
class Solution(object):
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        duplicateRecord = []
        for index, val in enumerate(numbers):
            if index == val:
                continue
            elif index != val and numbers[index] != numbers[val]:
                t = numbers[index]
                numbers[index] = numbers[val]
                numbers[val] = t
            elif index != val and numbers[index] == numbers[val]:
                duplicateRecord.append(numbers[index])

        if len(duplicateRecord) > 0:
            duplication[0] = duplicateRecord[0]
            return True
        else:
            return False
