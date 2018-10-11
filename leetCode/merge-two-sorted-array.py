# 给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，
# 使得 num1 成为一个有序数组。

# 说明:

# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
# 示例:

# 输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3

# 输出: [1,2,2,3,5,6]
[1,2,3,0,0,0]
[1,2,3]
[2,5,6]

3 < 6
[1,2,3,0,0,6]
[1,2,3]
[2,5, 6]

3 < 5
[1,2,3,0,5,6]
[1,2,3]
[2, 5, 6]

3 > 2
[1,2,3,3,5,6]
[1,2, 3]
[2, 5, 6]

2 = 2
[1,2,2,3,5,6]
[1,2, 3]
[ 2, 5, 6]

[1,2,2,3,5,6]

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # nums1 = nums1 + [0 for i in range(n)]
        if m == 0:
            return nums1
        elif n==0:
            return nums2
        else:
            sumLength = len(nums1)
            while m and n:
                if nums1[m-1] < nums2[n-1]:
                    nums1[sumLength-1] = nums2[n-1]
                    n -= 1
                elif nums1[m-1] > nums2[n-1]:
                    nums1[sumLength-1] = nums1[m-1]
                    m -= 1
                elif nums1[m-1] == nums2[n-1]:
                    nums1[sumLength-1] = nums2[n-1]
                    n -= 1
                    sumLength -= 1
                sumLength -= 1
            if m > 0:
                nums1[:sumLength] = nums1[:m-1]
            elif n > 0:
                nums1[:sumLength] = nums1[:m-1]
            
            return nums1
print(Solution().merge([1,2,3,0,0,0], 3, [2,5,6], 3))