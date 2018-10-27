# 给定两个非空链表来表示两个 非负 整数。位数按照逆序方式存储，
# 它们的每个节点只存储单个数字。将两数相加返回一个新的链表。

# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。

# 示例：

# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        return "{} -> {}".format(self.val, self.next)

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
l3 = ListNode(-1)
res = l3
nextValue = 0
while (l1.next or l2.next):
    value = l1.val + l2.val + nextValue
    if value / 10:
        value %= 10
        nextValue /= 10
    l3.next = ListNode(value)
    l1 = l1.next
    l2 = l2.next
if(nextValue):
    l3.next = ListNode(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return
        elif l1 is None and not l2 is None:
            return l1
        elif l2 is None and not l1 is None:
            return l2
        else:
            nextValue = 0
            l3 = ListNode(-1)
            res = l3
            while(l1 or l2):
                if l1 and l2:
                    value = l1.val + l2.val + nextValue
                elif not l1 and l2:
                    value = l2.val + nextValue
                elif not l2 and l1:
                    value = l1.val + nextValue
                else:
                    value = nextValue
                nextValue = value/10
                l3.next = ListNode(value%10)
                l3 = l3.next
                if l1:
                    l1 = l1.next
                if l2:
                    l2 = l2.next
            if (nextValue):
                l3.next = ListNode(1)
            return res.next