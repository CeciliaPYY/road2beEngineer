class Solution(object):
    def rob_without_one(self, subnums):
        if len(subnums) == 0:
            return 0
        elif len(subnums) == 1:
            return subnums[0]
        elif len(subnums) >= 2:
            dp = [0 for _ in range(len(subnums))]
            dp[0] = subnums[0]
            dp[1] = max(subnums[0], subnums[1])
            for i in range(2, len(subnums)):
                    max_dp = max([dp[j] for j in range(i-1)])
                    dp[i] = subnums[i] + max_dp
            return max(dp)
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            nums_no_first = nums[1:]
            nums_no_last = nums[:-1]
            return max(self.rob_without_one(nums_no_first), self.rob_without_one(nums_no_last))

