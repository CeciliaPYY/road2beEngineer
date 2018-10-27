# 环正建筑公司承包了Z市的一条道路的翻新工作。
# 新来的小张实习生将整个工程分为了n道工序，
# 按顺序进行每一步工序，
# 每一步工序都是将某一段区间 [Li, Ri] 的路段进行整修。
# 作为经理的你发现了小张的安排存在问题，许多工序是不必要的。
# 但是因为人员分配已经安排下去了，考虑到多方面的因素，
# 当工序x在工序y之前执行且工序y的区间完全包含了工序x的区间（x<y且Ly≤Lx<Rx≤Ry），
# 那么你可以撤销工序x。请问你最多能撤销掉多少步工序。
# n = 5
# tasks = [[1,5], [2,4], [2,3], [1,4], [2,5]]
def CCount(n, tasks):
    if n == 0:
        return 0
    else:
        count = 0
        for i in range(n-1, 0, -1):
            curStart = tasks[i][0]
            curEnd = tasks[i][1]
            for j in range(i-1, 0, -1):
                nextStart = tasks[j][0]
                nextEnd = tasks[j][1]
                if curStart <= nextStart and curEnd >= nextEnd:
                    count += 1
        return count/2

import sys
if __name__ == "__main__":
    n = int(raw_input())
    tasks = []
    for i in range(n):
        pairs = sys.stdin.readline().strip("\n").split(" ")
        for i in range(len(pairs)):
            pairs[i] = int(pairs[i])
        tasks.append(pairs)
    print(CCount(n, tasks))

