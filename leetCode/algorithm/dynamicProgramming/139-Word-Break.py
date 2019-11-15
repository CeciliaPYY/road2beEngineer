class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        slen = len(s)
        dp = [False]*(slen + 1)
        dp[0] = True

        for i in range(1, slen+1):
            for j in range(i):
                if dp[j] and (s[j:i] in wordDict):
                    dp[i] = True
        return dp[slen]
