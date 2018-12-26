# 题目：请实现一个函数，用来判断一棵二叉树是不是对称的。
# 如果一棵二叉树和它的镜像一样，那么它是对称的。

# 思路：只针对前序遍历的情况。如果我们定义一种对称前序遍历，
# 先遍历父节点，再遍历左子节点，最后遍历右子节点。那么如果一棵树的
# 前序遍历和它的对称前序遍历一致，我们就可以认为这是一棵对称二叉树。

# 我自己的做法是把两种遍历得到的结果都存储起来，最后看两者是否相等，
# 结果发现通过率只有10%，伤心....

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if pRoot is None:
            return False
        else:
            return Solution().preOrderLeftRight(pRoot) == Solution().preOrderRightLeft(pRoot)
    
    def preOrderLeftRight(self, node):
        preOrderLR = []
        if node is None:
            preOrderLR.append(None)
        else:
            preOrderLR.append(node.val)
            Solution().preOrderLeftRight(node.left)
            Solution().preOrderLeftRight(node.right)
        return preOrderLR

    def preOrderRightLeft(self, node):
        preOrderRL = []
        if node is None:
            preOrderRL.append(None)
        else:
            preOrderRL.append(node.val)
            Solution().preOrderRightLeft(node.right)
            Solution().preOrderRightLeft(node.left)
        return preOrderRL

# 作者的思想
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution2:
    def isSymmetrical(self, pRoot):
        # write code here
        return Solution2().isSymmetricalCore(pRoot, pRoot)
    
    def isSymmetricalCore(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        if (not node1.val == node2.val):
            return False
        
        return Solution2().isSymmetricalCore(node1.left, node2.right) and Solution2().isSymmetricalCore(node1.right, node2.left)