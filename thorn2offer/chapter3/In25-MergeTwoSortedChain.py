    # -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        return "{} -> {}".format(self.val, repr(self.next))
# class Solution:
#     # 返回合并后列表
#     def Merge(self, pHead1, pHead2):
#         # write code here


# 方法一：新建一个链表，然后比较两个链表中的元素值，
# 把较小的那个链到新链表中，由于两个链表的长度可能不同，
# 所以最终会有一个链表先完成插入所有元素，则直接将另一未完成
# 链表直接接入链表的末尾





class Solution(object):
    def mergeTwoSortedListNode(self, pHead1, pHead2):
        if pHead1 is None and pHead2 is None:
            return None
        elif not pHead1 is None and pHead2 is None:
            return pHead1
        elif not pHead2 is None and pHead1 is None:
            return pHead2
        else:
            # 创建两个链表指向同一结点，并且随意设置一个数作为起始
            pHead = dummy = ListNode(0)
            while pHead1 and pHead2:
                if pHead1.val < pHead2.val:
                    pHead.next = pHead1
                    pHead1 = pHead1.next
                else:
                    pHead.next = pHead2
                    pHead2 = pHead2.next
                pHead = pHead.next

            pHead.next = pHead1 or pHead2

            return dummy.next

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(9)

l2 = ListNode(4)
l2.next = ListNode(5)
l2.next.next = ListNode(7)

print(Solution().mergeTwoSortedListNode(l1,l2))
