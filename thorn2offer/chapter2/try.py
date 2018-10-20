# -*- coding:utf-8 -*-
class Solution:
    def hasPathCore(self, matrix, rows, cols, row, col, path, pathLength, visited):
        if pathLength == len(path):
            return True

        hasPath = False
        if (row >= 0 and row < rows and col >= 0 and col < cols and path[pathLength] == matrix[row][col] and not visited[row][col]):
            pathLength += 1
            visited[row*cols + col] = 1
            hasPath = self.hasPathCore(matrix, rows, cols, row-1, col, path, pathLength, visited) or self.hasPathCore(matrix, rows, cols, row+1, col, path, pathLength, visited) or self.hasPathCore(matrix, rows, cols, row, col-1, path, pathLength, visited) or self.hasPathCore(matrix, rows, cols, row, col+1, path, pathLength, visited)
            if not hasPath:
                pathLength -= 1
                visited[row*cols + col] = 0
        return hasPath

    def hasPath(self, matrix, rows, cols, path):
        # write code here
        visited = [0 for _ in range(cols*rows)]
        pathLength = 0
        for row in range(rows):
            for col in range(cols):
                if self.hasPathCore(matrix, rows, cols, row, col, path[1:], pathLength, visited):
                    return True
        return False

print(Solution().hasPath("ABCESFCSADEE",3,4,"ABCCED"))

