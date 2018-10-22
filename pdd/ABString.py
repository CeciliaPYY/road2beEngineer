# 题目描述：
# 给你两个正整数N和K，希望找到满足下面条件的字符串。     
# 字符串的长度为N，并且仅由’A’和’B’两个字符组成     
# 该字符串s刚好有K对（i，j），（0 <= i < j <= N-1）
# 满足s[i] = 'A'且 s[j] = 'B' 如果这样的字符串存在，
# 找到并返回字典序最大的一个，否则返回字符串 ”-“。

def maxDictValue(N, K):
    # N = 7
    # K = 3
    re = 0
    pairs = 0
    for i in range(0, K):
        re += i
        if re == K:
            pairs = re
    if not pairs == 0:
        stringList = []
        Bnums = N - (pairs-1)*2
        for i in range(Bnums):
            stringList.append('B')
        stringList.extend(['A','B']*(pairs-1))
        return ''.join(stringList)
    elif K%2 == 0:
        stringList = []
        for i in range(K):
            stringList.append('B')
        stringList.extend(['A']*(K/2))
        stringList.extend(['B']*(K/2))
    else:
        return




n = int(raw_input())
k = int(raw_input())
print(maxDictValue(n, k))

    # for i in range(1, (K-1)*2+1, 2):
    #     stringList[-i] = 'B'
    # for i in range(2, (K-1)*2+2, 2):
    #     stringList[-i] = 'A'
    # for n, i in enumerate(stringList):
    #     if i == False:
    #         stringList[n] = 'B'
    # result = ''.join(stringList)
    #     return result
    # else:


