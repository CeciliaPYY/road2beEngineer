# 题目：输入两棵二叉树 A 和 B，判断 B 是不是 A 的子结构。

# 要查找树 A 中是否存在和树 B 一样的子树，我们可以分成两步：
# 第一步，在树 A 中找到和 树 B 的根结点的值一样的节点 R；
# 第二步，判断树 A 中以 R 为根结点的子树是不是包含和 树 B 一样的结构。

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot1 is None or pRoot2 is None:
            return None
        else:
            result = False
            # 首先验证根结点值是否相等
            if (Solution().Equal(pRoot1.val, pRoot2.val)):
                result = Solution().DoesTree1HaveTree2(pRoot1, pRoot2)
            # 否则递归地匹配左右子节点
            if (not result):
                result = Solution().HasSubtree(pRoot1.left, pRoot2)
            if (not result):
                result = Solution().HasSubtree(pRoot1.right, pRoot2)
            return result

    def DoesTree1HaveTree2(self, tree1, tree2):
        # 如果树 B 遍历完成，那么则可以认为树 A 中包含树 B 
        if tree2 is None:
            return True
        # 如果树 B 遍历未完成，那么则可以认为树 A 中不包含树 B 
        if tree1 is None:
            return False
        # 若二者根结点不相等，则匹配失败
        if (not Solution().Equal(tree1.val, tree2.val)):
            return False
        # 若二者根结点相等，则继续递归匹配它们的左右子节点
        return Solution().DoesTree1HaveTree2(tree1.left, tree2.left) and Solution().DoesTree1HaveTree2(tree1.right, tree2.right)

    def Equal(self, num1, num2):
        if abs(num1 - num2) < 1e-6:
            return True
        else:
            return False