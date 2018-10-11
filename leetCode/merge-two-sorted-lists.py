# 有两个排序的数组 A1 和 A2，内存在 A1 的末尾有足够的空间容纳 A2。
# 实现一个函数，把 A2 中的所有数字插入  A1 中，并且所有数字都是排序的。

# 从尾到头比较 A1 和 A2 中的数字，并把较大的数字复制到 A1 的合适位置。
l1 = [1, 2, 3, 6, 7]
l2 = [4, 5, 9]

# [1, 2, 3, 6, 7, 9]
# [1, 2, 3, 5, 6, 7, 9]
# [1, 2, 3, 4, 5, 6, 7, 9]

combinL = l1 + [False for _ in range(len(l2))]
m1 = len(l1) - 1
m2 = len(l2) - 1
m = len(combinL) - 1

while m1 and m2:
    if l2[m2] > l1[m1]:
        combinL[m] = l2[m2]
        m2 -= 1
        m -= 1
    elif l2[m2] < l1[m1]:
        m1 -= 1
        combinL[m] = l1[m1]
        m -= 1
while m2:
    combinL[m] = l2[m2]
    m -= 1
    m2 -= 1
print(combinL)



