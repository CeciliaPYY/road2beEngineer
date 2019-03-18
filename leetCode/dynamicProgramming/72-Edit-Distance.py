class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        lenWord1 = len(word1)
        lenWord2 = len(word2)
        dp = [[0 for i in range(lenWord2 + 1)] for j in range(lenWord1 + 1)]
        for m in range(lenWord1+1):
            dp[m][0] = m

        for n in range(lenWord2+1):
            dp[0][n] = n

        for x in range(1, lenWord1 + 1):
            for y in range(1, lenWord2 + 1):
                if word1[x-1] == word2[y-1]:
                    dp[x][y] = min(dp[x-1][y] + 1, dp[x][y-1] + 1, dp[x-1][y-1])
                else:
                    dp[x][y] = min(dp[x-1][y] + 1, dp[x][y-1] + 1, dp[x-1][y-1] + 1)
        return dp[lenWord1][lenWord2]
