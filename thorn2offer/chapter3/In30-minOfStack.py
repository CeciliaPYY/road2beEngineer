# 题目：定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的min
# 函数。在该栈中，调用 min、push 及 pop 的时间复杂度都是O(1)

# 思路：用一个辅助栈存储每一次的最小值，就可以保证辅助栈栈顶始终为当前最小值
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, node):
        # write code here
        if not node is None:
            self.stack.append(node)
        if self.minStack == [] or node < self.min():
            # 如果最小栈为空 或者 当前节点值小于最小值，则压入最小栈中
            self.minStack.append(node)
        else:
            self.minStack.append(self.min())
            
    def pop(self):
        # write code here
        if self.stack == [] or self.minStack == []:
            return None
        else:
            self.minStack.pop()
            self.stack.pop()

    def top(self):
        # write code here
        return self.stack[-1]
        
    def min(self):
        # write code here
        return self.minStack[-1]