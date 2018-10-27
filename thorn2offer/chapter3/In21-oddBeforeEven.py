# 题目：输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
# 使得所有技术位于数组的前半部分，所有偶数位于数组的后半部分。
# [1,2,3,4,5] -> [1,5,3,4,2]

# 思路：二分法的思想
# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        if len(array) == 0:
            return 
        else:
            n = len(array)
            left = 0
            right = n - 1
            while(left < right):
                while(left < right and array[left] & 0x1 != 0):
                    left += 1
                while(left < right and array[right] & 0x1 == 0):
                    right -= 1
                if left < right:
                    # 只有满足偶数在奇数前面才进行交换
                    array[left], array[right] = array[right], array[left]
            return array

print(Solution().reOrderArray([1,2,3,4,5]))
print(Solution().reOrderArray([1,3,5,7,2,4,6]))
print(Solution().reOrderArray([1,2,3,4,5,6,7]))

# 如果面试官还要求：并保证奇数和奇数，偶数和偶数之间的相对位置不变。
# 这时候就不能用交换的思想了，因为交换必然会引起相对位置的变换
# 思路：先扫描数组，做三件事：1.奇数往前挪；2.统计偶数的个数；3.把偶数保存到队列中去
# -*- coding:utf-8 -*-
class Solution2:
    def reOrderArray(self, array):
        # write code here
        if array is None:
            return
        else:
            newArray = []
            n = len(array)
            for i in range(n):
                if array[i] & 0x1 != 0:
                    newArray.append(array[i])
                    array[i] = False
            evenArray = [e for e in array if not e == False]
            newArray.extend(evenArray)
            return newArray

print(Solution2().reOrderArray([1,2,3,4,5,6,7]))

# 如果你的面试官还给你提出什么乱七八糟的要求，比如1.把题目改成数组中的数按照大小分为两部分，
# 所有负数都在非负数的前面；2.把数组分为两部分，能被3整除的数都在不能被3整除的数的前面怎么办?
# 我们可以把这个把这个逻辑框架抽象出来，把判断的标准编程一个函数指针，也就是用一个单独的函数判断
# 数字是不是符合标准。解耦的好处就是提高了代码的重用性。
class Solution3():
    def reOrderArray(self, array, func):
        # write code here
        if len(array) == 0:
            return 
        else:
            n = len(array)
            left = 0
            right = n - 1
            while(left < right):
                while(left < right and func(array[left])):
                    left += 1
                while(left < right and func(array[right])):
                    right -= 1
                if left < right:
                    # 只有满足偶数在奇数前面才进行交换
                    array[left], array[right] = array[right], array[left]
            return array 
    def func(self, num):
        """
        1.奇数在偶数前面
        2.非负数在负数前面
        3.能被3整除的在不能被3整除的前面
        等等等
        """
            
