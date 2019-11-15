class Solution1(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)    
        nums1 = nums1 + [0 for _ in range(n)]
        length = m + n
             
        while m and n:
            if nums1[m-1] < nums2[n-1]:
                nums1[length-1] = nums2[n-1]
                n -= 1
            elif nums1[m-1] > nums2[n-1]:
                nums1[length-1] = nums1[m-1]
                m -= 1
            else:
                nums1[length-1] = nums1[m-1]
                length -= 1
                nums1[length-1] = nums2[n-1]
                m -= 1
                n -= 1
            length -= 1
        
        if m>0:
            nums1[:length] = nums1[:m]
        elif n>0:
            nums1[:length] = nums2[:n]
        print(nums1)
        
        if len(nums1)%2 == 0:
            median = (nums1[len(nums1)/2-1]+nums1[len(nums1)/2])/2.0
        else:
            median = nums1[(len(nums1)-1)/2]
        
        return median

# 归并排序，归并排序采用分组处理，即二分法的思想。将一组数据拆分为两组，
# 然后递归地将两个小组继续拆分，直到每个小组中剩下 1 个或 0 个元素。
# 这时才对小组中的元素进行合并，排序完成之后再合并成新的小组，一直往上
# 排序 和 合并 直到排序完成。具体参考：http://yshblog.com/blog/171
# 拆分部分
# [3,1,7,6,5,8,2,4]
# [3,1,7,6][5,8,2,4]
# [3,1][7,6][5,8][2,4]
# [3][1][7][6][5][8][2][4]

# 合并和排序部分
# [1,3][6,7][5,8][2,4]
# [1,3,6,7] [2,4,5,8]
# [1,2,3,4,5,6,7,8]
def split(nums):
    n = len(nums)
    if n <= 1:
        return nums
    else:
        mid = n // 2
        left = nums[:mid]
        right = nums[mid:]
        
        split(left)
        split(right)
