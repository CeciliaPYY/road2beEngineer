# 已知一个由小写英文字母a-z组成的字符串，
# 分别统计其中各个英文字母出现的次数，该字符串s的价值分为所有字母出现次数的平方和。 
# 现在你可以将其中的一个字母全部换成另一个任意的字母，修改后字符串的最大价值为多少？

import operator
def maxValue(string):
    hashString = dict.fromkeys([s for s in string])

    for k, v in hashString.items():
        hashString[k] = 0
    for s in string:
        hashString[s] += 1

    maxString = max(hashString.iteritems(), key=operator.itemgetter(1))[0]
    minString = min(hashString.iteritems(), key=operator.itemgetter(1))[0]
    maxStringTimes = hashString[maxString]
    minStringTimes = hashString[minString]

    del hashString[minString]
    hashString[maxString] += minStringTimes

    result = 0
    for k, v in hashString.items():
        result += v*v
    return result

if __name__ == "__main__":
    a = raw_input()
    print(maxValue(a))