# Given a collection of candidate numbers (candidates) 
# and a target number (target), find all unique combinations 
# in candidates where the candidate numbers sums to target.

# Each number in candidates may only be used once in the combination.

# Note:

# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations. (****重复的只算一次****)
# 去重可以通过 set 和 同一层不能使用同样的值 完成(i > s and candidates[i] == candidates[i-1])

# Example 1:
# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]

# Example 2:
# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
#   [1,2,2],
#   [5]
# ]

class Solution1(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        candidatesLength = len(candidates)
        result = []
        # used = [False] * candidatesLength

        self.dfs(target, 0, [], result, candidates)   

        mResult = []
        for res in result:
            if not res in mResult:
                mResult.append(res)     
        return mResult

    def dfs(self, mTarget, startPoint, cur, res, mCandidates):
        if mTarget == 0:
            res.append(cur[:])
            return
        for i in range(startPoint, len(mCandidates)):
            if mCandidates[i] > mTarget:
                break
            cur.append(mCandidates[i])
            self.dfs(mTarget - mCandidates[i], i + 1, cur, res, mCandidates)
            cur.pop()
        

class Solution2(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = []
        self.dfs(0, [], result, candidates, target)
        return result
    
    def dfs(self, startPoint, cur, res, mCandidates, mTarget):
        if mTarget == 0:
            res.append(cur[:])
            return 
        for i in range(startPoint, len(mCandidates)):
            if mCandidates[i] > mTarget:
                break
            if (i > startPoint) and (mCandidates[i] == mCandidates[i-1]):
                continue
            cur.append(mCandidates[i])
            self.dfs(i + 1, cur, res, mCandidates, mTarget - mCandidates[i])
            cur.pop()

        

if __name__ == "__main__":
    candidates = [10,1,2,7,6,1,5]
    target = 8
    # print(Solution1().combinationSum2(candidates, target))
    print(Solution1().combinationSum2(candidates, target))


