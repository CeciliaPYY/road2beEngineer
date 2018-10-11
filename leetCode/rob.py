# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，
# 影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
# 如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

# 给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置
# 的情况下，能够偷窃到的最高金额。

# [1, 2, 3, 1]
# dp = [1, 2, 1+3, 2+1] = [1, 2, 4, 3]
# max(dp) = 4

# [2, 7, 9, 3, 1]
# dp = [2, 7, 2+9, 3+7, 1+2+9] = [2, 7, 11, 10, 12]
# max(dp) = 12

# dp = [2, 1, 1+2, 2+2] = [2, 1, 3, 4]
# max(dp) = 4

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) >= 2:
            dp = [0 for _ in range(len(nums))]
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                    max_dp = max([dp[j] for j in range(i-1)])
                    dp[i] = nums[i] + max_dp
            return max(dp)




