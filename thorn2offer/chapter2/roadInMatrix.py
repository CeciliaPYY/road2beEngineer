# 请设计一个函数，用来判断在一个矩阵中是否存在一条
# 包含某字符串的所有字符的路径。
# 注意：1.路径可以从矩阵中的任意一格开始；
#      2.每一步可以在矩阵中向左、右、上、下移动一格；
#      3.如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子；
# mat = [['a', 'b', 't', 'g'],
#        ['c', 'f', 'c', 's'],
#        ['j', 'd', 'e', 'h']]
# target = 'bfce'
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
startIndex = []

# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if (matrix is None) or (rows < 1) or (cols < 1) or (path is None):
            return 
        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        # pathLength = 0
        