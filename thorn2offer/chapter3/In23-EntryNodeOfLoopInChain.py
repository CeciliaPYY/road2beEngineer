# 题目：如果一个链表中包含环，如何找出环的入口节点？

# 解决这个问题的第一步是如何确定一个链表中包含环。思路是定义两个指针，同时从链表的
# 头结点出发，一个指针一次走一步，另一个指针一次走两步。如果走得快的指针追上了走得慢
# 的指针，那么链表就包含环；如果走得快的指针走到了链表的末尾都没有追上第一个指针，那么
# 链表就不包含环。

def boolLoop(head):
    if head is None:
        return None
    else:
        fast = head
        slow = head
        while(fast.next):
            if fast.next.next:
                fast = fast.next.next
            else:
                fast = fast.next
            slow = slow.next
            if fast == slow:
                return fast
        return None

# 第二步是如何找到环的入口，还是可以用两个指针来解决这个问题。
# 先定义两个指针 p1 和 p2 指向链表的头结点。如果链表中的环有 n 个结点，则指针
# p1 就现在链表上向前移动 n 步，然后两个指针以相同的速度向前移动。当第二个指针
# 指向环的入口节点时，第一个指针已经绕着环走了一圈，又回到了入口节点。也就是说
# 这时候 p1 和 p2 相遇的结点正好是环的入口结点。

def searchEntry(head, lengthOfLoop):
    if head is None:
        return None
    else:
        p1 = head
        p2 = head

        for i in range(lengthOfLoop):
            p1 = p1.next

        while(not p1 == p2):
            p1 = p1.next
            p2 = p2.next
        
        return p1

# 剩下的问题是如何得到环中结点的数目。前面提到快慢指针的时候，快慢指针相遇的节点一定
# 是在环中，我们可以从这个节点出发，一边继续向前移动一边计数，当再次回到这个结点时，
# 就可以得到环中结点数了。
def lengthOfLoop(head):
    if head is None:
        return None
    else:
        nodesInLoop = 0
        fast = head
        slow = head
        meetingNode = None
        while (fast.next):
            if fast.next.next:
                fast = fast.next.next
            else:
                fast = fast.next
            if slow.next:
                slow = slow.next
            if fast == slow:
                meetingNode = fast
        track = slow
        while (track.next != meetingNode):
            track = track.next
            nodesInLoop += 1
        
        return nodesInLoop

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        # 首先先判断链表有没有环
        if pHead is None:
            return None
        elif not Solution().boolLoop(pHead):
            return None
        else:
            n = Solution().lengthOfLoop(pHead)
            if n == 0:
                return None
            else:
                return Solution().searchEntry(pHead, n)

    def boolLoop(self, head):
        if head is None:
            return None
        else:
            fast = head
            slow = head
            meetingNode = None
            nodesInLoop = 0
            while(fast.next):
                if fast.next.next:
                    fast = fast.next.next
                else:
                    fast = fast.next
                if slow.next:
                    slow = slow.next
                if fast == slow:
                    meetingNode = fast
            track = slow
            while (track.next != meetingNode):
                track = track.next
                nodesInLoop += 1
            if meetingNode == None:
                return None 
            else:
                return nodesInLoop

    def searchEntry(self, head, lengthOfLoop):
        if head is None:
            return None
        else:
            p1 = head
            p2 = head
            for i in range(lengthOfLoop):
                p1 = p1.next

            while(not p1 == p2):
                p1 = p1.next
                p2 = p2.next
            
            return p1

# 从第二步中可以知道，当链表快慢指针在环内相遇之后，如果将快指针指向头指针，慢指针不变
# 接下来，两个指针以相同速度开始遍历链表时，再次相遇的地方就是链表中环的入口
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution1:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if pHead is None:
            return False
        else:
            fast = pHead
            slow = pHead
            while(fast and fast.next):
                if fast.next.next:
                    fast = fast.next.next
                if slow.next:
                    slow = slow.next
                if fast == slow:
                    break
            # 如果快指针到达最后一个结点都没有追上慢指针，则返回null，即表中无环
            if fast == None or fast.next == None:
                return None
            fast = pHead
            while(not fast == slow):
                fast = fast.next
                slow = slow.next
            return fast

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        return "{} -> {}".format(self.val, self.next)

# if __name__ == "__main__":

pHead = ListNode(1)
pHead.next = pHead
print(Solution1().EntryNodeOfLoop(pHead))