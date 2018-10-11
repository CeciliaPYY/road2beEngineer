# Find the contiguous subarray within an array 
# (containing at least one number) which has the largest sum.

# For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
# the contiguous subarray [4,−1,2,1] has the largest sum = 6.

# 方法一：O(n)，思想如下
# [−2,1,−3,4,−1,2,1,−5,4]
# [1,-3,4,−1,2,1,−5,4]
# [1,-3,4,−1,2,1,−5,4]
# [4,−1,2,1,−5,4]
# [4,−1,2,1,−5,4]
# [4,−1,2,1]


class Solution(object):
    def maxSubArray(self, array):
        """
        :array type: list
        :return type: int
        """
        res = 0
        curSum = 0
        for i in range(len(array)):
            curSum = max(array[i], curSum+array[i])
            res = max(res, curSum)
        return res
        
print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

# 方法二（待补充），分治法