# 题目：输入一个链表的头结点，从尾到头反过来打印出每个节点的值。
# 要求，不能改变链表的结构

# 思路，从这道题看来，这是典型的“后进先出”的思想，我们可以用
# 栈实现这种顺序。

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    # def printListFromTailToHead(self, listNode):
        # write code here
p = ListNode(0)
p.next = ListNode(1)
while p.next:
    print(p.val)
    p.next = p

