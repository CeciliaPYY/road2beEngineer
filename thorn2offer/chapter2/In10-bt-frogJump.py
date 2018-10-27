# 题目描述
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
# 求该青蛙跳上一个n级的台阶总共有多少种跳法。

# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number == 0:
            return 0
        elif number == 1:
            return 1
        elif number == 2:
            return 2
        else:    
            resultFibonacci = [False for _ in range(number)]
            resultFibonacci[0] = 0
            resultFibonacci[1] = 1
            resultFibonacci[2] = 2
            for i in range(3, number):
                resultFibonacci[i] = sum([resultFibonacci[j] for j in range(0,i)]) + 1
            return sum(resultFibonacci) + 1

print(Solution().jumpFloorII(3))