# 题目：输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。
# 比如输入 3，则打印输出1、2、3一直到最大的 3 位数 999.

# 这个问题最主要的就是要考虑大数问题。

# 在字符串上模拟数字加法的解法，绕过陷阱才能拿到offer
# 最常用也是最容易的方法是使用字符串或者数组表达大数。数字最大是 n 位
# 的，因此我们需要一个长度为 n 的字符串。当实际数字不够 n 位的时候，
# 在字符串的前半部分补0.

# 具体思路如下：首先把字符串中的每一个数字都初始化为'0'，然后每一次为字符串
# 表示的数字加1，再打印出来。因此我们只需要做两件事，一是在字符串表达的数字
# 上面模拟加法；二是把字符串表达的数字打印出来。伪代码如下：
class Solution():
    def printToMaxOfNDigits(self, n):
        if n <= 0:
            return
        else:
            # 初始化一个字符串
            number = '0'*n
            while(not Solution().Increment(number)):
                Solution().PrintNumber(number)
            
    def Increment(self, number):
        # 实现在表示数字的字符串 number 上增加 1，如果达到最大的 n 位数，则返回 True
        if len(str(int(number) + 1)) > len(number):
            return True
        else:
            return False

    def PrintNumber(self, number):
        # 打印 number
        for i in range(len(number)):
            if not int(i) == 0:
                print(number)

# 看起来似乎很简单，但是这两个看似简单的函数都暗藏着小小玄机。
# 首先我们需要知道什么时候停止在 number 上加1，即达到了最大的 n 位数，
# 一个最简单的办法是在每次递增之后验证，是否有 int(number) == 最大的 n 位数，
# 但是对于长度为 n 的字符串，它的时间复杂度为O(n)。

# 但是我们注意到只有对 ’999...999‘(n个9)加 1 的时候，才会在第一个字符（下标为0）的基础上
# 产生进位，而其他所有情况都不会再第一个字符上产生进位。因此当我们发现在加 1 时第一个字符产生
# 了进位，则已经是最大的 n 位数，此时 Increment 返回 True，while循环终止，这样就实现了
# O(1)时间判断是不是已经达到了最大的 n 位数。
# 这个函数的具体实现方式见《剑指offer》

# 接下来再考虑如何打印用字符串表示的数字。这里主要是考虑打印要符合我们的阅读习惯，即
# 只有在碰到第一个非 0 的字符之后才开始打印，直到字符串的结尾。
