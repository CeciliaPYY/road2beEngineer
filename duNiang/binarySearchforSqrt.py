# 问题：现在没有开根号这个运算符，你如何写一个函数，即 y^2 = x，
# 在已知 x 的情况下，求得 y 的值。

# 以下是我面试的时候写的伪代码，回来 run 了一下是跑不通的，
# 可能是递归没写好的关系
import numbers
def binarySearchforSqrt(start, end, num):
    if not isinstance(num, numbers.Number):
        return 
    elif num < 0:
        return 
    elif num == 0:
        return 0
    elif num < 1:
        mid = 1/2
        if mid * mid > num:
            binarySearchforSqrt(0, mid, num)
        elif mid * mid < num:
            binarySearchforSqrt(mid, 1, num)
        elif abs(mid * mid - num) < 0.00000001:
            return mid
    else:
        mid = (num + 1) / 2
        if mid * mid > num:
            binarySearchforSqrt(1, mid, num)
        elif mid * mid < num:
            binarySearchforSqrt(mid, num, num)
        elif abs(mid * mid - num) < 0.00000001:
            return mid

# 在网上查阅了一下别人写的
# 首先先简单说一下思想，求平方根的算法主要有两种，分别是二分法和牛顿法
# 举个栗子，比如 x = 9 > 1
# 那么 (1 + 9)/2 = 5.0，而5.0 * 5.0 = 25.0 > 9
# 因此我会开始向下搜索，即 [1, 5.0]，继续折半
# 5.0 / 2 = 2.5，而 2.5 * 2.5 = 6.25 < 9，那我则开始向上搜索
# 即[2.5, 5]，这么一直做下去直到我找到的数字 abs(y * y - x) < delta
# 其中 delta 是一个很小的数字，比如十的负六次方

# 网上的很多代码都没有考虑被开方数小于1的情况，下面的代码是面试
# 的时候面试官提示之后在网上的版本上进行的一个修改
def mySqrt(num):
    if not isinstance(num, numbers.Number):
        return 
    elif num < 0:
        return
    elif num < 1:
        _max = 1.0
    else:
        _max = num
    _min = 0.0
    delta = 0.00000001
    mid = (_max + _min) / 2.0
    while((abs(mid * mid - num)) > delta):
        print(mid)
        if mid * mid < num:
            _min = mid
        elif mid * mid > num:
            _max = mid
        else:
            return mid
        mid = (_max + _min) / 2.0
    return mid

print(mySqrt(0.04)) # 0.199999988079
print(mySqrt(9)) # 3.0000000014

# 思路二：牛顿法求近似解
# 开根号的问题可以看做是求 f(x) = x^2 - a = 0 的根
def mySqrtNewton(num):
    if not isinstance(num, numbers.Number):
        return
    elif num < 0:
        return
    else:
        delta = 0.00000001
        x = 1.0
        while (abs(x*x - num) > delta):
            x = (x + num/x) / 2.0
        return x
print(mySqrtNewton(0.04)) # 0.200000000002
print(mySqrtNewton(9)) # 3.0000000014

# 以上代码参考：https://blog.csdn.net/u012348774/article/details/79804369