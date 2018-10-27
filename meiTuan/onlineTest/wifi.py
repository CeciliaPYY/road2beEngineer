# 一条直线上等距离放置了n台路由器。
# 路由器自左向右从1到n编号。
# 第i台路由器到第j台路由器的距离为| i-j |。

# 每台路由器都有自己的信号强度，
# 第i台路由器的信号强度为ai。
# 所有与第i台路由器距离不超过ai的路由器可以收到第i台路由器的信号（
# 注意，每台路由器都能收到自己的信号）。
# 问一共有多少台路由器可以收到至少k台不同路由器的信号。
def signalCount(n, k, power):
    count = 0
    if n == 0 or k == 0:
        return 
    if power[0] + 1 >= k:
        count += 1
    if power[n-1] + 1 >= k:
        count += 1
    for i in range(1,n-1):
        if 2*power[i] + 1 >= k:
            count += 1

    return count 

import sys
if __name__ == "__main__":
    res = []
    for i in range(2):
        line = sys.stdin.readline().strip("\n").split(" ")
        re = []
        for l in line:
            re.append(int(l))
        res.append(re)
    N = res[0][0]
    K = res[0][1]
    Power = res[1]
    print(signalCount(N,K,Power))