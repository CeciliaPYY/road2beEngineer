# 题目：Given an unsorted array of integers, find the length of longest increasing subsequence.

# For example,
# Given [10, 9, 2, 5, 3, 7, 101, 18],
# The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

# Your algorithm should run in O(n2) complexity.
# 大致思路如下：
# [10, 9, 2, 5, 3, 7, 101, 18]
# dp = [1, 1, 1, 1, 1, 1, 1, 1]
# dp[4] = dp[2] + 1 = 2
# dp = [1, 1, 1, 1, 2, 1, 1, 1] 
# dp[5] = dp[4] + 1 = 3
# dp = [1, 1, 1, 1, 2, 3, 1, 1] 
# dp[6] = dp[5] + 1 = 4
# dp = [1, 1, 1, 1, 2, 3, 4, 1] 

# -*- coding:utf-8 -*-

class AscentSequence:
    def findLongest(self, A, n):
        # write code here
        longestLength = [1 for i in range(n)]

        for i in range(n):
            for j in range(i):
                if A[j] < A[i]:
                    longestLength[i] = max(longestLength[i], longestLength[j]+1)
        return max(longestLength)
