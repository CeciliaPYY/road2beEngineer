# 给定 n 个气球，气球标号从 0 到 n-1。每个气球上都标有 nums 数组中的一个数字。
# 你需要把所有气球都弄破。如果你把第 i 个气球弄破了，你会得到 
# nums[left] * nums[i] * nums[right] 个硬币，这里的 left 和 right 都是 i
# 的邻近下标。当第 i 个气球弄破之后，left 和 right 就相邻了。
# 找到将所有气球弄破之后，你能得到的最大硬币值。

# 注意：nums[-1] = nums[n] = 1
# 0 <= n <= 500, 0 <= nums[i] <= 100

# Ex1
# Input: [3, 1, 5, 8]
# Output: 167


class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # first get some padding
        numsLength = len(nums)
        nums.insert(0, 1)
        nums.insert(len(nums), 1)

        # new a 2d array
        c  = [[0 for _ in range(len(nums))] for _ in range(len(nums))]

        for l in range(1, numsLength + 1):
            for i in range(1, numsLength - l + 2):
                j = i + l - 1
                for k in range(i, j + 1):
                    c[i][j] = max(c[i][j], c[i][k-1] + nums[i-1]*nums[k]*nums[j+1] + c[k+1][j])
        
        return c[1][numsLength]

if __name__ == "__main__":
    a = [3, 1, 5, 8]
    print(Solution().maxCoins(a))
