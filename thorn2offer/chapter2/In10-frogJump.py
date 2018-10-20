class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 0:
            return 0
        elif number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            resultFibonacci = [False for _ in range(number+1)]
            resultFibonacci[0] = 0
            resultFibonacci[1] = 1
            resultFibonacci[2] = 2
            for i in range(3, number+1):
                resultFibonacci[i] = resultFibonacci[i-1]+resultFibonacci[i-2]
            return resultFibonacci[number]
print(Solution().jumpFloor(0))
print(Solution().jumpFloor(1))
print(Solution().jumpFloor(2))
print(Solution().jumpFloor(3))
print(Solution().jumpFloor(4))