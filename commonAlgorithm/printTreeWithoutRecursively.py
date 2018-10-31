class Tree: 	
    def __init__(self, val, left = None, right = None):		
        self.val = val		
        self.left = left		
        self.right = right		
    
    def __str__(self):		
        return str(self.val) 
# 非递归实现二叉树的前序遍历

def PreOrderWithourRecursion(root):
    """
    1.利用栈，对每一个结点，先输入节点内容；
    2.若右子树不为空，则把右子树压入栈；
    3.若左子树不为空，则把左子树压入栈；
    """
    if root == None:
        return None
    stack = []
    node = root
    while(node or stack):

        while(node):
            stack.append(node.val)
            node = node.left

        node = stack.pop()
        node = node.right


