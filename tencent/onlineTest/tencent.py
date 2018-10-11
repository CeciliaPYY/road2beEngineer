import sys

if __name__ == "__main__":

    n  = sys.stdin.readline().strip()
    n = int(n)
    str1 = sys.stdin.readline().strip()
    str2 = sys.stdin.readline().strip()

    sub2 = {}
    for i in range(0,len(str2) - n + 1):
        sub2.setdefault(str2[i:i+n],0)
        sub2[str2[i:i+n]] += 1

    sub1 = {}
    for i in range(0,len(str1) - n + 1):
        sub1.setdefault(str1[i:i+n],0)
        sub1[str1[i:i+n]] += 1

    res = 0
    for k in sub1:
        try:
            res += sub2[k]
        except:
            pass

    print(res)