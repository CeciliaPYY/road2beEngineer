# -*- coding:utf-8 -*-
# 题目：输入一个字符串，打印出该字符串中的所有排列。例如，
# 输入字符串abc，则打印出由a、b、c所能排列出来的所有字符串
# abc、acb、bac、bca、cab 和 cba
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return None

ss = ["a", "b", "c"]
flag = 0
t = ss[flag]
ss[flag] = ss[flag+1]
ss[flag+1] = t
print(''.join(ss))

flag += 1
t = ss[flag]
ss[flag] = ss[flag+1]
ss[flag+1] = t
print(''.join(ss))

ss = ["a", "b", "c"]
flag = 0

