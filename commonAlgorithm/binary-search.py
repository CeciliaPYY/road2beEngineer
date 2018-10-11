# 二分查找又称折半查找，优点是比较次数少，查找速度快，平均性能好；
# 缺点是要求待查表为有序列表，且插入删除困难。因此折半查找适用于
# 不经常变动而查找频繁的有序列表。

# 首先，假设列表是按照升序排列，将表中间位置记录的关键字与待查找
# 关键字比较，若二者相等，则查找成功；否则利用中间位置记录将表
# 分成前后两个子表，若中间位置记录的关键字大于查找关键字，则进一步
# 查找前一子表，否则查找后一子表。重复以上过程，直到找到满足条件的
# 记录，使得查找成功，或直到子表不存在为止，此时查找不成功。

class Solution1(object):
    def binarySearch(self, nums, target):
        nums = sorted(nums)
        n = len(nums)
        start = 0
        end = n - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return False

class Solution2(object):
    def binarySearch2(self, nums, target):
        nums = sorted(nums)
        n = len(nums)
        if 0 == n:
            return False
        mid = n // 2
        if nums[mid] == target:
            return True
        elif nums[mid] > target:
            return Solution2().binarySearch2(nums[:mid], target)
        else:
            return Solution2().binarySearch2(nums[mid+1:], target)

print(Solution2().binarySearch2([2,1,5,4,3], 1))