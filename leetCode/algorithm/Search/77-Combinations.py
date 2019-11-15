# Given two integers n and k, return all possible
#  combinations of k numbers out of 1 ... n.

# Example
# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

def dfs(l, startPoint, cur, res, nums):
    # l : level
    # startPoint : start from where
    # cur : current state
    # res : main result
    # nums 
    if (len(cur) == l):
        res.append(cur[:])
        return
    for i in range(startPoint, len(nums)):
        cur.append(nums[i])
        dfs(l, i+1, cur, res, nums)
        cur.pop()

if __name__ == "__main__":
    n = 4
    k = 2
    nums = [i+1 for i in range(n)]
    ans = []
    dfs(k, 0, [], res, nums)



