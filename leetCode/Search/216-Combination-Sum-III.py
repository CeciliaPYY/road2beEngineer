# Find all possible combinations of k numbers that add up to a number n, 
# given that only numbers from 1 to 9 can be used and each combination 
# should be a unique set of numbers.

# Note:

# All numbers will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:

# Input: k = 3, n = 7
# Output: [[1,2,4]]
# Example 2:

# Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]

# dfs + backtracking
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        nums = [i+1 for i in range(9)]
        result = []
        self.dfs(k, n, 0, [], result, nums)
        return result

    def dfs(self, level, target, startPoint, cur, res, mNums):
        if (len(cur) == level) and target == 0:
            res.append(cur[:])
            return
        for i in range(startPoint, len(mNums)):
            if (i > startPoint) and (mNums[i] == mNums[i-1]):
                continue
            cur.append(mNums[i])
            self.dfs(level, target - mNums[i], i+1, cur, res, mNums)
            cur.pop()


# use 9 bit binary string to represent combination
# 000000000   -> []
# 000000001   -> [1]
# 000100011   -> [1,2,6]
# 111111110   -> [2,3,4,5,6,7,8,9]
# 111111111   -> [1,2,3,4,5,6,7,8,9]

# 1. if i-th bit is 1, then number[i+1] is used
# 2. total # of 1s should be k

class Solution2(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []

        for i in range(pow(2,9)):
            cur = []
            sum = 0
            for j in range(1, 9+1):
                if (i & (1 << (j-1))):
                    sum += j
                    cur.append(j)
            if (sum == n) and (len(cur) == k):
                result.append(cur)

        return result


if __name__ == "__main__":
    k = 3
    n = 9
    print(Solution().combinationSum3(k, n))
    print(Solution2().combinationSum3(k, n))