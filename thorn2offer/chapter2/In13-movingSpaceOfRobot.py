# 地上有一个m行和n列的方格。一个机器人从坐标 (0,0) 的格子开始移动，
# 每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐
# 标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），
# 因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。
# 请问该机器人能够达到多少个格子？


class Solution:
    def getSum(self, x):
        result = 0
        while(x):
            result += x % 10
            x /= 10
        return result

    def checkGrid(self, threshold, rows, cols, row, col, visited):
        if (row >= 0 and col >=0 and row < rows and col < cols and sum([self.getSum(row), self.getSum(col)]) <= threshold and not visited[row][col]):
            return True
        else:
            return False

    def movingCountCore(self, threshold, rows, cols, row, col, visited):
        # write code here
        count = 0
        if self.checkGrid(threshold, rows, cols, row, col, visited):
            visited[row][col] = 1
            count = 1 + self.movingCountCore(threshold, rows, cols, row-1, col, visited) + self.movingCountCore(threshold, rows, cols, row+1, col, visited) + self.movingCountCore(threshold, rows, cols, row, col-1, visited) + self.movingCountCore(threshold, rows, cols, row, col+1, visited)
        return count

    def movingCount(self, threshold, rows, cols):
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        return self.movingCountCore(threshold, rows, cols, 0, 0, visited)

