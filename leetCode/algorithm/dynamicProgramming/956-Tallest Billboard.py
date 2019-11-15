# You are installing a billboard and want it to have the largest height.  
# The billboard will have two steel supports, one on each side.  
# Each steel support must be an equal height.

# You have a collection of rods which can be welded together.  
# For example, if you have rods of lengths 1, 2, and 3, 
# you can weld them together to make a support of length 6.

# Return the largest possible height of your billboard installation.  
# If you cannot support the billboard, return 0.

# 3 Examples
# Ex1
# Input: [1,2,3,6]
# Output: 6
# Explanation: We have two disjoint subsets {1,2,3} and {6}, 
# which have the same sum = 6.

# Ex2
# Input: [1,2,3,4,5,6]
# Output: 10
# Explanation: We have two disjoint subsets {2,3,5} and {4,6}, 
# which have the same sum = 10.

# Ex3
# Input: [1,2]
# Output: 0
# Explanation: The billboard cannot be supported, so we return 0.

# Note
# 1. 0 <= rods.length <= 20 
# rods 这个 list 的长度介于 [0,20];
# 2. 1 <= rods[i] <= 1000
# 每根 rod 的长度介于 [1,1000];
# 3. The sum of rods is at most 5000.
# 所有 rods 的长度加载一起的总和最多 5000


# 每一根柱子都有 2 种状态，准确地来说是 3 种状态，即不被用；用于左边的柱子；用于右边的柱子；
# 这种情况下，如果直接用暴力搜索，时间复杂度为 O(3^N)。
# 除此之外，从 Note3 可以看出，我们选择的解决方法应该同 sum 有关，因此我们选择 DP 作为解决办法；

# 首先如果我们考虑动态数组中保存的是 两根柱子 h1 和 h2 的当前高度， 假设 h1 <= h2
# dp[i] 表示使用前 i 个柱子能够构成的柱子高度的集合
# 伪代码来一段

rods = [1,1,2]
dp = [False for i in range(len(rods)+1)]
dp[0] = [(0,0)]
for i in range(len(rods)+1):
    h = rods[i]
    for h1, h2 in dp[i-1]:
        dp[i] += (h1, h2) # 不使用
        dp[i] += (h1, h2+h) # 放在高的那一边
        if h1 + h < h2:
            dp[i] += (h1+h, h2) # 放在低的那一边
        else:
            dp[i] += (h2, h1+h) # 放在低的那一边


