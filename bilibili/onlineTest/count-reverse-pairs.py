nums = [9, 11, 3, 6, 4]

# 方法一：冒泡法思想 (AC=0.25)
# -*- coding:utf-8 -*-
class Solution1(object):
    def InversePairs(self, data): 
        n = len(data)
        res = 0 
        for i in range(n):
            for j in range(i+1, n):
                if data[i] > data[j]:
                    res += 1
                else:
                    continue
        return res%1000000007

# 方法二：(AC=50%)
class Solution2(object):
    def InversePairs(self, data):
        res = 0
        sortedData = sorted(data)
        for i in sortedData:
            pos = data.index(i)
            res += pos
            data.pop(pos)
        return res%1000000007

# 方法三：用归并排序的思想
# class Solution3(object):
#     def InversePairs(self, data):
#         n = len(data)
#         if n == 0 or n == 1:
#             return 0
#         else:
res = 0
data = [9, 11, 3, 6, 4]
n = len(data)
mid = n // 2
nums1 = data[:mid]
m1 = len(nums1)
nums2 = data[mid:]
m2 = len(nums2)
nums1 = nums1 + [0 for _ in range(m2)]
while m1 and m2:
    if nums1[m1-1] < nums2[m2-1]:
        nums1[n-1] = nums2[m2-1]
        m2 -= 1
    elif nums1[m1-1] > nums2[m2-1]:
        nums1[n-1] = nums1[m1-1]
        m1 -= 1
        res += m1
    else:
        nums1[n-1] = nums1[m1-1]
        n -= 1
        nums1[n-1] = nums2[m2-1]
        m1 -= 1
        m2 -= 1
    n -= 1
            # if m1 > 0:
            #     nums1[:n] = nums1[:m1]
            # elif m2 > 0:
            #     nums1[:n] = nums2[:m2]
            # return res
# print(Solution3().InversePairs([9, 11, 3, 6, 4]))

                    


