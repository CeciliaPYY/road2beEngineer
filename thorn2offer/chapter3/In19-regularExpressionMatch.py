# 题目：请实现一个函数用来匹配包含'.'和'*'的正则表达式。模式中的
# 字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）
# 在本题中，匹配是指字符串的 所有 字符 匹配 整个 模式。例如字符串"aaa"
# 与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。

# -*- coding:utf-8 -*
# class Solution():
# def match(self, s, pattern):
def match(s, pattern):
    if len(s) == 0 and len(pattern) == 0:
        return True
    elif len(s) == 0 and len(pattern) == 2 and pattern[-1] == "*":
        return True
    else:
        # return Solution().matchCore(0, s, 0, pattern)
        return matchCore(0, s, 0, pattern)

# def matchCore(self, sIndex, s, patternIndex, pattern):
def matchCore(sIndex, s, patternIndex, pattern):
    if (sIndex == len(s) - 1) and (patternIndex == len(pattern) - 1 ):
        return True

    if (not sIndex == len(s) - 1) and (patternIndex == len(pattern) - 1 ):
        return False

    if pattern[patternIndex + 1] == '*':
        if s[sIndex] == pattern[patternIndex] or (pattern[patternIndex] == '.' and not sIndex == len(s)):
            return  matchCore(sIndex + 1, s, patternIndex + 2, pattern) or matchCore(sIndex + 1, s, patternIndex, pattern) or matchCore(sIndex, s, patternIndex + 2, pattern)
            # return  Solution().matchCore(sIndex + 1, s, patternIndex + 2, pattern) or Solution().matchCore(sIndex + 1, s, patternIndex, pattern) or Solution().matchCore(sIndex, s, patternIndex + 2, pattern)
        else:
            return matchCore(sIndex, s, patternIndex + 2, pattern)

    if s[sIndex] == pattern[patternIndex] or (pattern[patternIndex] == '.' and not sIndex == len(s)):
        return matchCore(sIndex + 1, s, patternIndex + 1, pattern)
    
    return False
    
print(match("a", ".*"))