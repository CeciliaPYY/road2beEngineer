# 题目：实现函数 double Power(double base, int exponent)，求 base 的 exponent
# 次方。不得使用库函数，同时不需要考虑大数问题。

# 这个题目最主要的是要注意到输入的指数 exponent 小于 1 的时候我们要怎么办？
# -*- coding:utf-8 -*-
class Solution1:
    def Power(self, base, exponent):
        # write code here
        if base == 0 and exponent == 0:
            return 1
        elif base == 0:
            return 1
        elif exponent == 0:
            return 1
        elif exponent < 0:
            return 1/(Solution1().Power(base, (-1)*exponent))
        else:
            result = 1.0
            for i in range(exponent):
                result *= base
            return result

# 既全面又高效的解法，确保我们能拿到 offer
# pow(x, 32) = pow(pow(x, 16),2) = pow(pow(pow(x, 8),2),2)

# -*- coding:utf-8 -*-
class Solution2:
    def Power(self, base, exponent):
        # write code here
        if base == 0 and exponent == 0:
            return 1
        elif base == 0:
            return 1
        elif exponent == 0:
            return 1
        elif exponent < 0:
            return 1/(Solution2().Power(base, (-1)*exponent))
        else:
            result = 1.0
            result = (Solution2().Power(base, exponent >> 1))
            result *= result
            if (exponent & 0x1 == 1):
                return result * base
            else:
                return result
# 注意，从上述代码中可以看到我们用右移运算代替了除以2，用位与运算符代替了求余运算符
# 来判断一个数是奇数还是偶数。位运算的效率比乘除及求余运算的效率要高很多。