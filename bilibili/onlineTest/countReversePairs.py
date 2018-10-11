import sys
import copy

def InversePairs(data):
    sortData = sorted(data)
    count = 0
    for i in sortData:
        pos = data.index(i)
        count += pos
        data.pop(pos)
    return count


if __name__ == "__main__":

    n = sys.stdin.readline().strip()
    values = map(int, sys.stdin.readline().strip().split())
    ls = []
    for v in values:
        ls.append(v)

    reverse_count = dict.fromkeys(range(len(ls)))

    for i in range(len(ls)):
        ls_new = copy.deepcopy(ls)
        ls_new[i] = 0
        reverse_count[i] = InversePairs(ls_new)


    for k, v in reverse_count.items():
        if v == min(reverse_count.values()):
            print(v)
            print(k+1)