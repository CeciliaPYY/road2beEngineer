# 给你一根长度为n的绳子，请把绳子剪成m段 (m和n都是整数，n>1并且m>1)
# 绳子长度至少为2，且绳子至少剪一段（**）
# 每段绳子的长度记为k[0],k[1],...,k[m-1].
# 请问k[0]*k[1]*...*k[m-1]可能的最大乘积是多少？
# 例如，当绳子的长度为8时，我们把它剪成长度分别为2,3,3的三段，此时得到的最大乘积是18.
# 从题目可以看出，这道题目有着动态规划题目所有的特点，可被分解为相互重叠的小问题，
# 大问题的最优解等于小问题的最优解的组合。

# 动态规划的解决
class Solution1():
    def cutRope(self, ropeLength):
        if ropeLength <= 1:
            return 0
        elif ropeLength == 2:
            return 1
        elif ropeLength == 3:
            return 2
        else:
            subDp = [0 for _ in range(ropeLength+1)]
            subDp[1] = 1
            # 当绳子长度大于2的时候，把2剪开没有不剪开面积大
            subDp[2] = 2
            # 当绳子长度大于3的时候，把3剪开没有不剪开面积大
            subDp[3] = 3
            for i in range(4, ropeLength+1):
                re = []
                for j in range(1, i):
                    re.append(subDp[j]*subDp[i-j])
                subDp[i] = max(re)
            return subDp[-1]

print(Solution1().cutRope(4))
print(Solution1().cutRope(5))
print(Solution1().cutRope(6))
print(Solution1().cutRope(8))

# 贪婪算法
# 如果我们按照如下的策略来剪绳子，则得到的各段绳子的长度乘积将最大；
# 当n大于等于5时，我们尽可能多剪长度为3的绳子，因为很容易可以证明
# 2*(n-2) > n, 3*(n-3) > n 且3 *(n-3) > 2*(n-2)
# 当剩下的绳子长度为 4 时，把绳子简称两段长度为 2 的绳子
class Solution2():
    def cutRope(self, ropeLength):
        if ropeLength <= 1:
            return 0
        elif ropeLength == 2:
            return 1
        elif ropeLength == 3:
            return 2
        else:
            cutTime2 = cutTime3 = 0
            if ropeLength >= 5:
                cutTime3 = ropeLength // 3
                ropeLength %= 3
            if ropeLength == 4:
                cutTime2 = ropeLength // 2
                ropeLength %= 2
            if ropeLength == 0:
                return pow(3, cutTime3) * pow(2, cutTime2)
            else:
                return pow(3, cutTime3) * pow(2, cutTime2) * ropeLength

print(Solution2().cutRope(4))
print(Solution2().cutRope(5))
print(Solution2().cutRope(6))
print(Solution2().cutRope(8))