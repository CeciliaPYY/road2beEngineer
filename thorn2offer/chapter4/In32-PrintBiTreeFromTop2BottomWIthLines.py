# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    # 返回从上到下每个节点值列表，例：[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if pRoot is None:
            return []
        else:
            nodeList = [] 
            valueList = [] 
            nodeList.append(pRoot)
            while nodeList:
                size = len(nodeList)
                result = []

                for n in nodeList:
                    result.append(n.val)

                valueList.append(result)

                for i in range(size):
                    currentNode = nodeList.pop(0)
                    if currentNode.left:
                        nodeList.append(currentNode.left)
                    if currentNode.right:
                        nodeList.append(currentNode.right)
            
            return valueList

