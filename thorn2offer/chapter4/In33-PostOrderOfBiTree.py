# -*- coding:utf-8 -*-
# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。
# 如果是则返回 true，否则返回 false。假设输入数组的任意两个
# 数字都互不相同。
# 例子1：[5,7,6,9,11,10,8]
# 8 为根结点
# [5,7,6]左子树都比8小，[9,11,10]右子树都比8大
# 6 为左子树的根结点，10为右子树的根结点
# 5为左子树的左子节点且比6小，7为左子树的右子节点且比6大；
# 9为右子树的左子节点且比10小，11为右子树的右子节点且比10大；
# 例子2：[7,4,6,5]
# 5为根结点
# 7 > 5，因此该树没有左子树只有右子树
# 但是 4 < 5，因此该数组不是二叉搜索树的后序遍历

class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if sequence == []:
            return False
        else:
            # 假设现在已经退化到只有一颗树了[5,7,6]
            # [5,7,6] 8 [9,11,10]
            root = sequence[-1] # root = 6 root = 8
            for i in range(len(sequence)):
                if sequence[i] > root: # i = 1 i=4
                    break

            for j in range(i, len(sequence)-1):
                if sequence[j] < root:
                    return False

            leftSubTree = sequence[:i]
            rightSubTree = sequence[i:-1]

            left = True
            if i > 0:
                left = Solution().VerifySquenceOfBST(leftSubTree)
            
            right = True
            if i < len(sequence) - 1:
                right = Solution().VerifySquenceOfBST(rightSubTree)

            return left and right