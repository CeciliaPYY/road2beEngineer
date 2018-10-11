# 给定一个矩阵m，从左上角开始每次只能向右或者向下走，最后到达右
# 下角的位置，路径上所有的数字累加起来就是路径和，返回所有的路径
# 中最小的路径和。
# 思路：求最值，一般想到的做法就是动态规划。举个例子，
# 1 3 5 9
# 8 1 3 4
# 5 0 6 1
# 8 8 4 0
# 1-3-1-0-6-1-0 = 12
# 则很容易可以得到转移方程为：
# dp[i][j] = m[i][j] + min(dp[i][j-1],dp[i-1][j])
A = [[1,3,5,9], [8,1,3,4], [5,0,6,1], [8,8,4,0]]
dp = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]
dp[0][0] = A[0][0]
# 1 3 5 9
for i in range(1, len(A[0])):
    dp[i][0] = A[i][0] + dp[i-1][0]
for j in range(1, len(A)):
    dp[0][j] = A[0][j] + dp[0][j-1]

for i in range(1,len(A[0])):
    for j in range(1, len(A)):
        dp[i][j] = A[i][j] + min(dp[i-1][j], dp[i][j-1])

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # if grid == None:
        #     return 0
        # else:
nrow = len(grid)
ncol = len(grid[0])
dp = [[0 for _ in range(ncol)] for _ in range(nrow)]
for i in range(1, nrow):
    dp[i][0] = grid[i][0] + dp[i-1][0]

for j in range(1, ncol):
    dp[0][j] = grid[0][j] + dp[0][j-1]

for i in range(1, nrow):
    for j in range(1, ncol):
        dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
    
        return dp[nrow-1][ncol-1]

print(Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
grid = [[1,3,1],[1,5,1],[4,2,1]]