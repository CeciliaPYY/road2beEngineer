def minMoves22(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    median = sorted(nums)[len(nums) / 2]
    return sum(abs(num - median) for num in nums)

import sys
numOfBuilding = int(sys.stdin.readline().strip("\n"))
need = int(sys.stdin.readline().strip("\n"))
Nums = []
Nums.append(int(s for sys.stdin.readline().strip("\n").split(" "))
print(minMoves22(Nums) - need)