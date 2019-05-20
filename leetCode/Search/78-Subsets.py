# Given a set of distinct integers, nums, return all possible subsets (the power set).
# Note: The solution set must not contain duplicate subsets.

# Example:
# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for i in range(len(nums)+1):
            self.dfs(i, 0, [], nums, res)

        return res
    
    def dfs(self, level, startPoint, cur, nums, result):
        if len(cur) == level:
            result.append(cur[:])
            return
        for i in range(startPoint, len(nums)):
            cur.append(nums[i])
            self.dfs(level, i+1, cur, nums, result)
            cur.pop()

if __name__ == "__main__":
    nums = [1,2,3]
    print(Solution().subsets(nums))