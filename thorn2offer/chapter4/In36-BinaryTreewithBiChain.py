# -*- coding:utf-8 -*-
# 题目：输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
# 要求不能创建任何新的节点，职能调整书中节点指针的指向。

# 将二叉搜索树转换成排序双向链表，原先指向左子节点的指针调整为链表中
# 指向前一个结点的指针，原先指向右子节点的指针调整为链表中指向后一个
# 结点的指针

class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return
        self.attr = []
        self.ConvertCore(pRootOfTree)
        for k, v in enumerate(self.attr[:-1]):
            # 将每一个结点的右节点作为它的下一个节点
            v.right = self.attr[k+1]
            # 将每一个节点下一个节点的左节点即为该节点本身
            self.attr[k+1].left = v
        
        return self.attr[0]

    def ConvertCore(self, node):
        if not node:
            return
        # 中序遍历才是从小到大
        self.ConvertCore(node.left)
        self.attr.append(node)
        self.ConvertCore(node.right)