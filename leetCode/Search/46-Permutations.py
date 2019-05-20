# Given a collection of distinct integers, return all possible permutations.

# Example:
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        numsLength = len(nums)
        used = [False] * numsLength
        result = []
        self.dfs(numsLength, 0, [], nums, result, used)
        return result

    def dfs(self, level, startPoint, cur, nums, ans, mUsed):
        if len(cur) == level:
            ans.append(cur[:])
            return 
        for i in range(len(nums)):
            if mUsed[i]: 
                continue
            mUsed[i] = True
            cur.append(nums[i])
            self.dfs(level, i, cur, nums, ans, mUsed)
            cur.pop()
            mUsed[i] = False

if __name__ == "__main__":
    nums = [1,2,3] 
    print(Solution().permute(nums))
   
