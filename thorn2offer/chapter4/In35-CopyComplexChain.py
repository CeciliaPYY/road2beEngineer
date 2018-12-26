# 题目：复杂链表的复制
# 实现函数复制一个复杂链表。在复杂链表中，每个结点除了有一个m_pNext指针指向下一个节点，
# 还有一个 m_pSibling 指针指向链表中的任意节点或者 nullptr。

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        Solution().CloneNodes(pHead)
        Solution().ConnectSiblingNodes(pHead)
        return Solution().ReconnectNodes(pHead)

    # 第一步 复制原始链表的任意结点 N 并创建新节点 N’，再把 N’ 链接到 N 的后面
    def CloneNodes(self, pHead):
        pNode = pHead
        while(pNode):
            pCloned = RandomListNode(pNode.label)
            pCloned.next = pNode.next # 复制原链表的节点
            pNode.next = pCloned # 将原链表的节点指向复制的链表
            pNode = pCloned.next # 将复制链表的节点指向原链表

    # 第二步 设置复制出来的节点的 m_pSibling，假设原始链表上的 N 的
    # m_pSibling 指向节点 S，那么其对应复制出来的 N‘ 是 N 的 m_pNext
    # 指向的节点，同样 S' 也是 S 的 m_pNext 指向的节点。
    def ConnectSiblingNodes(self, pHead):
        pNode = pHead
        while(pNode):
            pclone = pNode.next
            if pNode.random:
                pclone.random = pNode.random.next
            pNode = pclone.next
    
    # 第三步，把这个长链表拆分成两个链表，把奇数位置的节点用 m_pNext 连接
    # 起来就是原始链表，把偶数位置的节点用 m_pNext 连接起来就是复制出来的
    # 链表。
    def ReconnectNodes(self, pHead):
        pNode = pHead
        pCloneHead = None
        pCloneNode = None
        if pNode:
            pCloneHead = pCloneNode = pNode.next
            pNode.next = pCloneNode.next
            pNode = pNode.next
        while pNode:
            pCloneNode.next, pCloneNode = pNode.next, pCloneNode.next
            pNode.next, pNode = pCloneNode.next, pNode.next
        return pCloneHead
