# 题目：请实现一个函数，输入一个整数，输出该二进制表示中1的个数。

# 思路一：可能引起死循环的解法
# 1.正数情况下的基本思路：先判断正数二进制表示中最右边一位是不是1；
# 接着把输入的正数右移一位，此时原来处于最右边起的第二位被移到最右边了，再判断是不是；
# 这样每次移动一位直到整个整数变为 0 为止。那么如何判断一个整数的最右边是不是 1 呢，
# 很简单只要把整数和 1 做位与运算就好了。但是这种情况下可能出现的一个问题是，当输入的
# 数字为负数时，右移的过程同样要保证最高位仍然为负，因此移位后的最高位会设为 1，随后
# 就会陷入死循环。

# 思路二：为了避免上述情况的产生，我们可以不右移输入的数字 n，而是将做 位与运算 的 1
# 进行左移，这样反复左移并做位与运算就可以判断 n 的其中一位是否为1.

# -*- coding:utf-8 -*-
class Solution1:
    def NumberOf1(self, n):
        # write code here
        count = 0
        flag = 1
        while flag:
                if n & flag:
                        count += 1
                flag = flag << 1
        return count 

# 在上面的方法中，循环的次数等于整数二进制的位数，32位的整数需要循环32次。
# 思路二：把一个整数减去1，再和原整数做与运算，会把该整数最右边的 1 变为 0。
# 那么一个整数的二进制表示中有多少个1，就可以进行多少次这样的操作。
class Solution2:
    def NumberOf1(self, n):
        # write code here
        if n == 0:
                return 0
        else:
                count = 0
                while(n&0xffffffff != 0):
                        count += 1
                        n = n & (n - 1)
                return count
# 注意：为什么要把 while(n) 改为 while(n&0xffffffff != 0) 呢？
# 详情请见 https://blog.csdn.net/u010005281/article/details/79851154

# 相关题目：1.用一条语句判断一个整数是否为 2 的整数次方
# 思路：一个整数如果是 2 的整数次方，那么它的二进制中有且只有一位是1，其他位置
# 均为0，因此我们将该数字和该数字减去1之后的结果做位与运算，这个整数中唯一的 1
# 就会变为 0.
class Solution3:
    def is2Power(self, n):
        # write code here
        if n == 0:
                return False
        else:
                if n & (n-1) == 0:
                        return True
                else:
                        return False

# 相关题目2：输入两个整数 m 和 n，计算需要改变 m 的二进制表示中的多少位，才能得到 n。
# 思路：即求 m 和 n 中不同的位一共有多少，可以分为两步，一先计算 m 和 n 的异或，而计算
# 两者异或结果中 1 的个数
class Solution4:
        def m2N(self, m, n):
                mnDiff = m ^ n
                return Solution1().NumberOf1(mnDiff)

# 结论：把一个整数减去 1 之后再和原来的整数做位与运算，得到的结果相当于把整数的二进制
# 表示中最右边的 1 变为 0.很多二进制的问题都可以利用这种思路解决。