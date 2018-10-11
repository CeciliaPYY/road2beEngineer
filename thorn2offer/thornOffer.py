# 题目描述
# 输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        return "{}->{}".format(self.val, repr(self.next))

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        head_array = []
        while(head):
            head_array.append(head.val)
            head = head.next

        return [head_array[i] for i in range(len(head_array)-1, -1, -1)]

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        ls = []
        while(listNode):
            ls.append(listNode.val)
            listNode = listNode.next
        return [ls[i] for i in range(len(ls)-1, -1, -1)]


