# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        blankSpaceNum = 0
        # 统计字符串中的空格数目
        for i in range(len(s)):
            if s[i] == ' ':
                blankSpaceNum += 1

        # 创建一个新的字符串，它的长度为将所有空格替换为 20% 之后的长度
        newS = list(s) + [False for _ in range(blankSpaceNum*2)]

        # 设置两个指针，一个指针位于原字符串的末尾，另一指针位于新字符串的末尾
        m = len(list(s)) - 1
        n = len(newS) - 1
        while m and n:
            if newS[m] != ' ':
                t = newS[n]
                newS[n] = newS[m]
                newS[m] = t
                m -= 1
                n -= 1
            else:
                m -= 1
                newS[n] = '0'
                newS[n - 1] = '2'
                newS[n - 2] = '%'
                n -= 2
            if m == n:
                break
        return newS
print(Solution().replaceSpace("We are happy"))


