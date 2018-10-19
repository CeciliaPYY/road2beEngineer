# 题目二：不修改数组找出重复的数字
# 一个长度为 n+1 的数组中，所有数字都介于 1~n 范围之内，
# 因此该数组至少有一个数字是重复的。
# 要求：找出数字中任意一个重复数字，要求不能修改输入的数组

# 思路一：遍历原数组，将数组中每一个数字的值放在一个新数组中
# 与值相等的坐标位置处
class Solution(object):
    def duplicate(self, numbers, duplication):
        copyNumbers = []
        duplicationRecord = []
        for i in range(len(numbers)):
            if copyNumbers[numbers[i]]:
                duplicationRecord.append(numbers[i])
            else:
                copyNumbers[numbers[i]] = numbers[i]
        if len(duplicationRecord) > 0:
            duplication[0] = duplicationRecord[0]
            return True
        else:
            return False

# 思路二：首先确定数组的范围，然后将其一分为二，分别判断每一部分中的
# 数字在数组中重复出现的次数，将其同这一部分的元素个数进行比较；如果
# 大于后者，则意味着这一部分中存在重复数字；否则，则不存在重复数字
class Solution2(object):
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        maxNum = max(numbers)
        minNum = min(numbers)
        
