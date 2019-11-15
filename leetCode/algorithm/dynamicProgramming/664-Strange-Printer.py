# 有一个奇怪的打印机，必须满足以下两个要求：
# 1. 这个打印机每次只可以打印一连串相同的字母；
# 2. 每次转换的时候，打印机可以从任意一个地方开始打印或结束打印，并且会覆盖原有的字母；

# 给定一个只包含小写字母的字符串，寻找打印该字符串的最小打印次数。

# Ex 1
# Input: "aaabbb"
# Ouput: 2

# Ex 2
# Input: "aba"
# Ouput: 2

# 注意给定字符串的长度不会超过100

# 首先尝试使用记忆化递归
class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        slength = len(s)

        # initialize
        self.t_ = [[0 for _ in range(slength)] for _ in range(slength)]
        return self.turn(s, 0, slength - 1)
    
    def turn(self, s, i, j):
        if (i > j):
            return 0

        if self.t_[i][j] > 0:
            return self.t_[i][j]
        
        # 默认最差情况下，
        ans = self.turn(s, i, j-1) + 1

        for k in range(i, j):
            if s[k] == s[j]:
                ans = min(ans, self.turn(s, i, k) + self.turn(s, k+1, j-1))

        self.t_[i][j] = ans
        return self.t_[i][j]

if __name__ == "__main__":
    s1 = "aaabbb"
    print(Solution().strangePrinter(s1))
    s2 = "aba"
    print(Solution().strangePrinter(s2))



