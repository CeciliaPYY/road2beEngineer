# 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""。

# 示例 1:
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 示例 2:

# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 说明:
# 所有输入只包含小写字母 a-z 。
# strs = ["flower","flow","flight"]


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return
        minLength = min([len(strs[i]) for i in range(len(strs))])
        shortestString = []
        for string in strs:
            if len(string) == minLength:
                shortestString.append(string)

        res = 0
        for i in range(minLength):
            targetChar = shortestString[0][i]
            re = 0
            for j in range(len(strs)):
                if strs[j][i] == targetChar:
                    re += 1
            if re == len(strs):
                res += 1
        if res == 0:
            return ""
        else:
            return shortestString[:res]

print(Solution().longestCommonPrefix(["dog","racecar","car"]))