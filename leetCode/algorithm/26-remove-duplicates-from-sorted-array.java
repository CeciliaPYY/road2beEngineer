package com.company;

import java.util.*;

public class Solution {
    public int removeDuplicates(int[] nums) {
        // 我之前的想法是如果nums中的元素后一个和前一个一样，则数组长度不变，移除元素本身，
        // 如果后一个元素和前一个元素不一样，那么数组长度+1，但其实这种做法是因为题目本身
        // 具有误导性，想误导你去改变数组本身，但这样的过程中数组的长度是变化的，你无法通过
        // fori的方法去跑完整个数组，那么我们就换一种思想，不改变数组本身。

        // 选用两个指针，其中快指针负责跑完整个数组，慢指针负责记录两个指针指向的元素是否相同，如果
        // 相同则慢指针不动，如果不同慢指针+1，整个过程中快指针每经过一次操作都+1
        // 还有就是还是要修改数组
        int fast = 0;
        int slow = 0;
        int numsLength = nums.length;

        while (fast < numsLength) {
            if (nums[fast] == nums[slow]) {
                fast++;
            } else  {
                nums[++slow] = nums[fast++];
            }

        }

        return slow + 1;

    }

    public static void main(String[] args) {
        int[] nums = {0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
        Solution solution = new Solution();
        System.out.println(solution.removeDuplicates(nums));
    }
}
