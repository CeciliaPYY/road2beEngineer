# -*- coding:utf-8 -*-
# 题目：请实现两个函数，分别用来序列化和反序列化二叉树。
# 序列化：将一棵二叉树转变为一个字符串
# 反序列化：所谓反序列化是根据一个字符串重新建立一棵二叉树

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    flag = -1
    def Serialize(self, root):
        # write code here
        # if not root:
        #     return
        if not root:
            return None
        biString = []
        result = []
        if not root:
            return
        else:
            biString.extend(self.SerializeCore(root, result))

        return biString
    
    def SerializeCore(self, root, result):
        if not root:
            result.append('#')
            return
        result.append(root.val)
        self.SerializeCore(root.left, result)
        self.SerializeCore(root.right, result)
        return result

    def Deserialize(self, s):
        # write code here
        """
        设置一个指针指向序列的最开始，然后把指针指向位置的数字转化为二叉树的节点
        后移一个数字，转化为左子树和右子树。当遇到当前指向的字符为特殊字符或者指针
        超出字符串长度时，返回None，指针后移，继续遍历
        """
        if not s:
            return None
        self.flag += 1  ####很巧妙的一步#####
        if self.flag >= len(s):
            return None
        
        root = None
        if s[self.flag] != '#':
            root = TreeNode(int(s[self.flag]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        
        return root

if __name__ == "__main__":
    tree = TreeNode(1)
    tree_l = TreeNode(2)
    tree_r = TreeNode(3)
    tree_ll = TreeNode(4)
    tree_rl = TreeNode(5)
    tree_rr = TreeNode(6)
    tree_l.left = tree_ll
    tree_r.left = tree_rl
    tree_r.right = tree_rr
    tree.left = tree_l
    tree.right = tree_r
    s = Solution().Serialize(tree)
    print(s)
    print(Solution().Deserialize(s))

