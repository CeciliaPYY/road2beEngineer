#-*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        return "{} -> {}".format(self.val, self.next)
        
# 思路一：交换指针        
class Solution1:
    def ReverseList(self, pHead):
        f = ListNode(-1)
        q = pHead
        while(True):
            if q == None:
                break
            else:
                # 首先事先保存 q 的之后所有节点，记为 r
                r = q.next 
                # 将当前节点的链表方向反转
                q.next = f.next
                # 更新最后要输出的反转链表
                f.next = q 
                # 开始处理剩下的节点
                q = r

        return f.next

# 思路二：存储结点值，反向输出
class Solution2:
    def ReverseList(self, pHead):
        if pHead is None:
            return None
        else:
            array = []
            while(pHead):
                array.append(pHead.val)
                pHead = pHead.next
            rHead = newHead = ListNode(-1)
            for i in range(len(array)-1, -1, -1):
                newHead.next = ListNode(array[i])
                newHead = newHead.next
            return rHead.next

