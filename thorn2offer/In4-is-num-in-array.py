# 题目：在一个二维数组中，每行从左到右依次递增，
# 每列从上到下依次递增。完成一个函数，给定一个这样的二维数组和
# 任意一个数字，判断数组中是否有该整数。
# -*- coding:utf-8 -*-
class Solution2(object):
    def Find(self, target, array):
        rowNums = len(array)
        colNums = len(array[0]) 
        colNum = 0
        rowNum = len(array) - 1
        while rowNum >= 0 and colNum < colNums:
            if array[rowNum][colNum] == target:
                return True
            elif array[rowNum][colNum] < target:
                colNum += 1
            elif array[rowNum][colNum] > target:
                rowNum -= 1
        return False


# -*- coding:utf-8 -*-
class Solution1(object):
    # array 二维列表
    def Find(self, target, array):
        # write code here
        rownums = len(array)
        rownum = 0
        colnum = len(array[0]) - 1
        while rownum < rownums and colnum >= 0:
            if target < array[rownum][colnum]:
                colnum -= 1
            elif target > array[rownum][colnum]:
                rownum += 1
            elif target == array[rownum][colnum]:
                return True
        return False