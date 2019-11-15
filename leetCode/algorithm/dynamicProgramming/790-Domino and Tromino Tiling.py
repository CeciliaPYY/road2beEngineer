class Solution:
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        mod = 1000000007
        dp = [[0] * 2 for _ in range(N+1)]
        dp[0][0] = 1
        dp[1][0] = 1
        for i in range(2, N+1):
            # case 1，完整覆盖
            dp[i][0] = (dp[i-1][0] + dp[i-2][0] + 2 * dp[i-1][1]) % mod
            # case 2，第一行或者第二行突出
            dp[i][1] = (dp[i-2][0] + dp[i-1][1]) % mod
        
        return dp[N][0]

if __name__ == "__main__":
    N = 3
    print(Solution().numTilings(N))