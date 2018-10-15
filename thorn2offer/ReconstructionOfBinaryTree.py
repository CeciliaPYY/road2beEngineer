preOrder = [1,2,4,7,3,5,6,8]
inOrder = [4,7,2,1,5,3,6,8]
# preOrder[0] 即为根结点的值，所以 inOrder 中[4,7,2]是左子树结点的值，
# inOrder 中[5,3,6,8]是右子树结点的值,同样的 preOrder 
# 中[2,4,7]是左子树结点的值，preOrder 中[3,5,6,8]是右子树结点的值

class tree:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.val)

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        nPre = len(pre)
        nIn = len(tin)
        if nPre == 0 or nIn == 0 or nPre != nIn:
            return None
        else:
            root = pre[0]
            rootIndexInOrder = tin.index(root)
            inOrderLeft = tin[:rootIndexInOrder]
            inOrderRight = tin[rootIndexInOrder+1:]
            preOrderLeft = pre[1:len(inOrderLeft)+1]
            preOrderRight = pre[1+len(inOrderLeft):]
            left = Solution().reConstructBinaryTree(preOrderLeft, inOrderLeft)
            right = Solution().reConstructBinaryTree(preOrderRight, inOrderRight)
            return tree(root, left, right)

print(Solution().reConstructBinaryTree([1,2,4,7,3,5,6,8], [4,7,2,1,5,3,6,8]))



