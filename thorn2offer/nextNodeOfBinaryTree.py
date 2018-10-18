# 给定一棵二叉树和其中一个节点，如何找出中序遍历序列的下一个节点？
# 树中的节点除了有两个分别指向左、右子节点的指针，还有一个指向
# 父节点的指针
# 还是先来看一个例子，比如一棵二叉树的中序遍历为 [d, b, h, e, i, a, f, c, g]
# 我们对每种情况进行分析：
# 对于像 b, a, c, e 这种有右子树的节点，有 b->a, a->f, c->g, e->i, 因此
# 需要从右子节点出发一直沿着指向左子节点的指针；
# 对于像 d, f 和 h 这种没有右子树，而且它们是所属父节点的左子节点的点，有
# d->b, f->c, h->e, 因此可以总结出这种类型的点的下一节点就是它们的父节点；
# 对于像 i 和 g 这样没有右子树，并且它还是父亲节点的右子节点的情况就比较复杂。
# 我们可以沿着父节点的指针一直向上遍历，直到找到一个是它父节点的左子节点的节点。
# 这样的节点如果存在，那么这个节点的父节点记为我们要找的下一个节点；否则该节点
# 不存在下一节点。

# -*- coding:utf-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return 
        if pNode.right:
            temp = pNode.right
            while temp.left:
                temp = temp.left
            return temp
        else:
            if pNode.next is None:
                return 
            elif pNode == pNode.next.left:
                    return pNode.next
            else:
                if pNode.next == pNode.next.next.left:
                    return pNode.next.next
                else:
                    return 


