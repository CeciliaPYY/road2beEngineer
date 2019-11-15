# Given a set of candidate numbers (candidates) 
# (without duplicates) and a target number 
# (target), find all unique combinations 
# in candidates where the candidate numbers sums to target.

# The same repeated number may be chosen from candidates 
# unlimited number of times.(candidates 可以重复使用)

# Note:

# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.

# Example 1:

# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
#   [7],
#   [2,2,3]
# ]

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = []
        self.dfs( target , 0, [], result, candidates)
        return result

    def dfs(self, mTarget, startPoint, cur, res, mCandidatess):
        if (mTarget == 0):
            res.append(cur[:])
            return
        for i in range(startPoint, len(mCandidatess)):
            if (mCandidatess[i] > mTarget):
                break 
            cur.append(mCandidatess[i])
            self.dfs(mTarget - mCandidatess[i], i, cur, res, mCandidatess)
            cur.pop()

if __name__ == "__main__":
    candidates = [2,3,6,7]
    target = 7
    print(Solution().combinationSum(candidates, target))
    
    