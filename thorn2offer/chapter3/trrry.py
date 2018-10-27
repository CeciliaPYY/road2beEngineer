#-*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def ReverseList(self, pHead):
        if pHead is None:
            return None
        else:
            array = []
            while(pHead):
                array.append(pHead.val)
                pHead = pHead.next
            newHead = ListNode(-1)
            for i in range(len(array)-1, 0, -1):
                newHead.next = ListNode(array[i])
                newHead = newHead.next
            return newHead
p = ListNode(1)
p.next = ListNode(2)
p.next.next = ListNode(3)
p.next.next.next = ListNode(4)
p.next.next.next.next = ListNode(5)

print(Solution().ReverseList(p))

            