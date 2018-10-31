# 题目：输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

# 思路：可以把矩阵想象成若干个圈。然后用一个循环来打印矩阵，每次打印矩阵中的一个圈。
# 打印一般假设从左上角开始，容易得到左上角的坐标为的行列坐标总是相同的，
# 因此会选取(start, start)作为我们的分析目标。

# 同样我们会发现，在 5x5 和 6x6 的矩阵中最后一圈左上角的坐标都为(2,2)，
# 且我们有 5 > 2*2 以及 6 > 2*2
# 于是可以得出循环继续的条件是 columns > startX * 2 and rows > startY * 2

# 然后考虑如何打印一圈的功能，打印一圈可以分为四步，
# 第一步，从左到右打印一行；第二步，从上到下打印一列；
# 第三步，从右到左打印一行；第四步，从下到上打印一列；
# 每一步根据起始坐标和终止坐标就能打印出一列或者一行

# -*- coding:utf-8 -*-
class Solution:

    def printMatrix(self, matrix):
        # write code here
        # matrix类型为二维列表，需要返回列表
        if matrix is None:
            return 

        rows = len(matrix)
        columns = len(matrix[0])

        if rows <= 0 or columns <= 0:
            return

        start = 0
        result = []
        while(rows > start * 2 and columns > start * 2):
            result.extend(Solution().printMatrixCore(matrix, columns, rows, start))
            start += 1
        
        return result
    
    def printMatrixCore(self, numbers, columns, rows, start):
        endX = columns - 1 - start
        endY = rows -1 - start
        res = []
        for i in range(start, endX + 1):
            res.append(numbers[start][i])
        if (start < endY):
            # 如果至少有两行，那么则执行第二步
            for i in range(start + 1, endY + 1):
                res.append(numbers[i][endX])
        if (start < endX and start < endY):
            # 如果至少有两行两列，那么则执行第三步
            for i in range(endX - 1, start - 1, -1):
                res.append(numbers[endY][i])
        if (start < endX and start < endY - 1):
            for i in range(endY - 1, start, -1):
            # 如果至少有三行两列，那么则执行第三步
                res.append(numbers[i][start])
        return res

if __name__ == "__main__":
    mat = [[1,2],[3,4]]
    print(Solution().printMatrix(mat))

# 但是值得注意的是，这样的圈可能会退化成一行或者一列，甚至只有一个数字
# 因此需要仔细分析打印每一步前的需要满足的前提条件
# 可以得到，第一行总是需要打印的；需要打印第二步的条件是终止行号大于起始行号
# 需要打印第三步的条件是至少有两行两列，即终止行号大于起始行号，终止列号大于起始列号
# 需要打印第四步的前提条件是至少有三行两列，即终止行号起码比起始行号大2，且终止列号大于起始列号
  