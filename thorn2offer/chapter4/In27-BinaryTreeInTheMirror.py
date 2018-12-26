# 题目：请完成一个函数，输入一个二叉树，该函数输出它的镜像。

# 思路：通过画图的方法很容易发现，
# 这道题目的做法就是在遍历树的同时交换非叶结点的左右子节点。

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root is None:
            return None
        # 如果遇到叶子结点则不交换
        if root.left is None and root.right is None:
            return None
        
        # 交换左右子节点
        temp = root.left
        root.left = root.right
        root.right = temp

        # 如果是非叶子结点，则继续交换
        if(root.left):
            Solution().Mirror(root.left)
        if(root.right):
            Solution().Mirror(root.right)



            
