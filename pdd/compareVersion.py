def compareVersion(version1, version2):
    """
    :type version1: str
    :type version2: str
    :rtype: int
    """
    v1_split = version1.split('.')
    v2_split = version2.split('.')
    v1_len, v2_len = len(v1_split), len(v2_split)
    maxLen = max(v1_len, v2_len)
    for i in range(maxLen):
        temp1, temp2 = 0, 0
        if i < v1_len:
            temp1 = int(v1_split[i])
        if i < v2_len:
            temp2 = int(v2_split[i])
        if temp1 < temp2:
            return -1
        elif temp1 > temp2:
            return 1
    return 0

import sys
string1 = raw_input()
string2 = raw_input()
print(compareVersion(string1, string2))
