# 求链表的中间节点，如果链表中的节点总数为奇数，则返回中间节点；
# 如果节点总数是偶数，则返回中间两个节点的任意一个。

# 为了解决这个问题，我们也可以定义两个指针，同时从链表的头结点出发，
# 一个指针一次走一步，另一个指针一次走两步。当走得快的指针走到链表的
# 末尾时，走得慢的指针正好在链表的中间。

class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution():
    def findMiddleNode(self, head):
        if head is None:
            return None
        else:
            fast = head
            slow = head
            while (fast.next):
                if fast.next.next:
                    fast = fast.next.next
                else:
                    fast = fast.next
                slow = slow.next
                print(fast.val, slow.val)
            return slow.val

p = ListNode(1)
p.next = ListNode(2)
p.next.next = ListNode(3)
p.next.next.next = ListNode(4)
p.next.next.next.next = ListNode(5)
p.next.next.next.next.next = ListNode(6)
print(Solution().findMiddleNode(p))