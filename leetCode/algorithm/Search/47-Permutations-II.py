# Given a collection of numbers that might contain 
# duplicates, return all possible unique permutations.

# Example:
# Input: [1,1,2]
# Output:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        numsLength = len(nums)
        result = []
        used = [False] * numsLength

        self.dfs(numsLength, 0, [], result, nums, used)

        return result

    def dfs(self, level, startPoint, cur, res, nums, mUsed):
        if len(cur) == level:
            res.append(cur[:])
            return
        for i in range(len(nums)):
            if mUsed[i]:
                continue
            if (i > 0) and (nums[i] == nums[i-1]) and (mUsed[i-1] == False):
                continue
            mUsed[i] = True
            cur.append(nums[i])
            self.dfs(level, i, cur, res, nums, mUsed)
            cur.pop()
            mUsed[i] = False

if __name__ == "__main__":
    nums = [1,1,2]
    print(Solution().permuteUnique(nums))

