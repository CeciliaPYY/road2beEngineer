
def partition(nums, left, right):
    pivot = len(nums) - 1
    while left < right:
        while left < right and nums[left] <= nums[pivot]:
            left += 1
        while left < right and nums[right] >= nums[pivot]:
            right -= 1
        nums[left], nums[right] = nums[right], nums[left]

    nums[right], nums[pivot] = nums[pivot], nums[right]
    return left

def quickSort(nums, start, end):
    left = partition(nums, start, start)
    quickSort(nums, 0, left-1)
    quickSort(nums, left, len(nums)-1)

quickSort([3,7,8,5,2,1,9,5,4], 0, 8)






