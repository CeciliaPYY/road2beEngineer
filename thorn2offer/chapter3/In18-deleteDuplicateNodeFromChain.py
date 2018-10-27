# 题目描述
# 在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，
# 重复的结点不保留，返回链表头指针。 
# 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5


p = ListNode(1)
p.next = ListNode(2)
p.next.next = ListNode(3)
p.next.next.next = ListNode(3)
p.next.next.next.next = ListNode(4)
p.next.next.next.next.next = ListNode(4)
p.next.next.next.next.next.next = ListNode(5)

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        return "{}->{}".format(self.val, self.next)
class Solution:
    def deleteDuplication(self, pHead):
        if pHead is None or pHead.next is None:
            return pHead
        else:
            # 将链表里面的值都存到一个数组里面去
            array = []
            array.append(pHead.val) 
            while pHead.next:
                pHead = pHead.next
                array.append(pHead.val)
            array = list(pHead)
            # 建立一个字典存储链表中每个值出现的次数
            count = dict.fromkeys(array)
            # 首先初始化它
            for k, v in count.items():
                count[k] = 0
            # 存储频数
            for i in range(len(array)):
                count[array[i]] += 1
            
            # 如果链表中的值出现超过一次，就将他们记录下来
            duplicateList = []
            for k, v in count.items():
                if v > 1:
                    duplicateList.append(k)  

            # 保留只在链表中出现过一次的值
            restNode = [n for n in array if n not in duplicateList]
            return restNode, duplicateList, array

# 本来想通过上面这种思路解决这个问题的，但是发现输入一直调整不好
# 牛客的实例输入为：{1,2,3,3,4,4,5}；输出为：{1,2,5}
# 因此还是参考了剑指offer上的思路
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead is None or pHead.next is None:
            return pHead
        else:
            head1 = ListNode(pHead.val - 1)
            head1.next = pHead
            firstNode = head1
            secondNode = pHead
            while secondNode and secondNode.next:
                if secondNode.val == secondNode.next.val:
                    delVal = secondNode.val
                    while(secondNode and secondNode.val == delVal):
                        secondNode = secondNode.next
                    firstNode.next = secondNode
                else:
                    firstNode = firstNode.next
                    secondNode = secondNode.next
            
            return head1.next
                    

