# 链表中倒数第 k 个结点
# 题目：输入一个链表，输出该链表中倒数第 k 个结点。为了符合大多数人的习惯
# 本题从 1 开始计数，即链表的尾结点是倒数第一个结点。例如，一个链表有 6 个结点。
# 从头结点开始，他们的值依次是1、2、3、4、5、6，这个链表的倒数第 3 个结点是值
# 为 4 的节点。

# 思路一：另开辟一个空间
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def FindKthToTail(self, head, k):
        # write code here
        if head is None or k <= 0:
            return 
        else:
            array = []
            while(head):
                array.append(head.val)
                head = head.next
            return array[-k]

p = ListNode(1)
p.next = ListNode(2)
p.next.next = ListNode(3)
p.next.next.next = ListNode(4)
p.next.next.next.next = ListNode(5)

print(Solution1().FindKthToTail(p,3))
print(Solution1().FindKthToTail(p,1))

# 思路二：由于这是一个单项链表，因此我们不能从尾结点开始遍历这个链表。那么还是把思路返回到
# 头结点上。假设整个链表有 n 个结点，那么倒数第 k 个结点就是顺数第 n-k+1 个结点。我们为了
# 得到链表的总结点数 n，需要完整遍历一遍链表。这种思路下我们需要遍历链表两次。
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution2:
    def FindKthToTail(self, head, k):
        # write code here
        if head is None or k <= 0:
            return
        else:
            p = head
            n = 0
            while(p):
                n += 1
                p = p.next
            for i in range(n-k):
                head = head.next
            return head

p = ListNode(1)
p.next = ListNode(2)
p.next.next = ListNode(3)
p.next.next.next = ListNode(4)
p.next.next.next.next = ListNode(5)
p.next.next.next.next.next = ListNode(6)

print(Solution2().FindKthToTail(p, 3))

# 然后你的面试官期待的解法是只需要遍历链表一次
# 为了实现只遍历一遍链表就能找到倒数第 k 个结点，我们可以定义两个指针。
# 第一个指针从链表的头指针开始遍历向前走 k-1 步，此时第二个指针保持不动；
# 从第 k 步开始第二个指针也开始从链表的头指针开始遍历。由于两个指针的
# 距离始终保持在 k-1，当第一个指针到达链表的尾部时，第二个指针正好指向
# 倒数第 k 个结点。

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head is None or k <= 0:
            return None
        else:
            pFirst = head
            pSecond = head
            for i in range(k-1):
                # 加入链表中结点数小于k，则返回None
                if pFirst.next == None:
                    return None
                pFirst = pFirst.next
            while (not pFirst.next == None):
                pFirst = pFirst.next
                pSecond = pSecond.next
            
            return pSecond





