# 现在要求输入一个整数n，请你输出斐波那契数列的第n项
# （从0开始，第0项为0）n <= 39

# -*- coding:utf-8 -*-
# 递归法，出现运行超时
class Solution1:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return Solution1().Fibonacci(n-1) + Solution1().Fibonacci(n-2)

n = 5
# F[5] = F[4] + F[3]
# F[4] = F[3] + F[2]
# F[3] = F[2] + F[1]
# F[2] = F[1] + F[0]
resultFibonacci = [False for _ in range(n)]
resultFibonacci[0] = 0
resultFibonacci[1] = 1
for i in range(2,5):
    resultFibonacci[i] = resultFibonacci[i-1]+resultFibonacci[i-2]

class Solution2:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            resultFibonacci = [False for _ in range(n+1)]
            resultFibonacci[0] = 0
            resultFibonacci[1] = 1
            for i in range(2, n+1):
                resultFibonacci[i] = resultFibonacci[i-1]+resultFibonacci[i-2]
            return resultFibonacci[n]

# 注意：青蛙跳级以及小矩形覆盖大矩形的问题都可以转化成斐波那契数列问题