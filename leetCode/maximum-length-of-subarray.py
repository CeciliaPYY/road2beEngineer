# Given two integer arrays A and B, return the maximum length of an subarray 
# that appears in both arrays.

# Example 1:
# Input:
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# Output: 3
# Explanation: 
# The repeated subarray with maximum length is [3, 2, 1].
# Note:
# 1 <= len(A), len(B) <= 1000
# 0 <= A[i], B[i] < 100
# e.g 思路如下
# A = [3,1,2]
# B = [1,2,2] 
#   3 1 2 
# 1 0 1 0
# 2 0 0 2 
# 2 0 0 1



class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        m = len(A)
        n = len(B)
        longestLength = 0
        dp = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                if A[i] == B[j]:
                    dp[i][j] = 1
                    longestLength = max(longestLength, dp[i][j])

        for i in range(1, m):
            for j in range(1, n):
                if dp[i-1][j-1] and A[i] == B[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    longestLength = max(longestLength, dp[i][j])

        return longestLength