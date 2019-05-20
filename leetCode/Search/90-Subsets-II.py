# Given a collection of integers that might contain duplicates, 
# nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

# Example:
# Input: [1,2,2]
# Output:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in range(len(nums) + 1):
            self.dfs(i, 0, [], result, nums)
        
        return result

    def dfs(self, level, startPoint, cur, res, mNums):
        if len(cur) == level:
            res.append(cur[:])
            return
        for i in range(startPoint, len(mNums)):
            if (i > startPoint) and (mNums[i] == mNums[i-1]):
                continue
            cur.append(mNums[i])
            self.dfs(level, i + 1, cur, res, mNums)
            cur.pop()


if __name__ == "__main__":
    nums = [1,2,2]
    print(Solution().subsetsWithDup(nums))

