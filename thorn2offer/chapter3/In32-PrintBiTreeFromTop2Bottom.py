# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if root is None:
            return []
        else:
            nodeList = [] # 用来装结点
            valueList = [] # 用来装结点值
            nodeList.append(root)
            while nodeList:
                currentNode = nodeList.pop(0)
                valueList.append(currentNode.val)
                if currentNode.left:
                    nodeList.append(currentNode.left)
                if currentNode.right:
                    nodeList.append(currentNode.right)
            return valueList

tree = TreeNode(8, TreeNode(6,5,7), TreeNode(10,9,11))
print(Solution().PrintFromTopToBottom(tree))
            
