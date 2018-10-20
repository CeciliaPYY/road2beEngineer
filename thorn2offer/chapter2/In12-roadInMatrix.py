# 请设计一个函数，用来判断在一个矩阵中是否存在一条
# 包含某字符串的所有字符的路径。
# 注意：1.路径可以从矩阵中的任意一格开始；
#      2.每一步可以在矩阵中向左、右、上、下移动一格；
#      3.如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子；
mat = [['a', 'b', 't', 'g'],
       ['c', 'f', 'c', 's'],
       ['j', 'd', 'e', 'h']]
target = 'bfce'
#        b 
#     /  |  \
#    a   t   f 
#          / | \
#         c  c  d 
#        /  / \
#       j  s   e
# 这是一个可以用回溯法解决的典型题。首先在矩阵中任选一个点作为路径的起点。
# 假设矩阵中某个格子的字符是ch，并且这个格子将对应于路径上的第i个字符。
# 若路径上的第i个字符不是ch，那么这个格子不可能处在路径上的第i个位置。
# 如果路径上的第i个字符正好是ch，那么到相邻的格子寻找路径上第i+1个字符。
# 除矩阵边界上的格子之外，其他格子都有4个相邻的格子。重复这个过程，直到路径
# 上的所有字符都在矩阵中找到相应的位置。
# 由于路径不能重复进入矩阵的格子，所以还需要定义和字符矩阵大小一致 的布尔值
# 矩阵，用来标识路径是否已经进入了每个格子。

# 首先应该判断特殊情况
# 然后....
mat = [['a', 'b', 't', 'g'],
       ['c', 'f', 'c', 's'],
       ['j', 'd', 'e', 'h']]
m = len(mat)
n = len(mat[0])
target = 'bfce'
# -*- coding:utf-8 -*-
class Solution:
    def hasPathCore(self, matrix, rows, cols, row, col, path, pathLength, visited):
        if pathLength == len(path):
            # 说明已经完成了全部的匹配过程
            return True

        hasPath = False
        if (row >= 0 and row < rows and col >= 0 and col < cols and path[pathLength] == matrix[row*cols + col] and not visited[row*cols + col]):
            pathLength += 1
            visited[row*cols + col] = 1
            hasPath = self.hasPathCore(matrix, rows, cols, row-1, col, path, pathLength, visited) or self.hasPathCore(matrix, rows, cols, row+1, col, path, pathLength, visited) or self.hasPathCore(matrix, rows, cols, row, col-1, path, pathLength, visited) or self.hasPathCore(matrix, rows, cols, row, col+1, path, pathLength, visited)
            if not hasPath:
                # 如果不匹配则回溯
                pathLength -= 1
                visited[row*cols + col] = 0
        return hasPath

    def hasPath(self, matrix, rows, cols, path):
        # write code here
        # 建立一个轨迹矩阵，记录走过的格子
        visited = [0 for _ in range(cols*rows)]
        pathLength = 0
        # 这种方法没有预先直接定位到path[0]，而是先在matrix里面寻找path[0]
        for row in range(rows):
            for col in range(cols):
                if self.hasPathCore(matrix, rows, cols, row, col, path, pathLength, visited):
                    return True
        return False
print(Solution().hasPath("ABCESFCSADEE",3,4,"ABCCED"))