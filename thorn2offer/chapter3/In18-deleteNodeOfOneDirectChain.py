# 题目：在O(1)时间内删除链表结点
# 给定单项链表的头指针和一个节点指针，定义一个函数在O(1)时间内删除该节点。

# 在单向链表中删除一个节点，常规的做法无意识从链表的头节点开始，
# 顺序遍历查找要删除的节点，并在链表中删除该节点，但是这种按照顺序查找的思路，
# 时间复杂度就是O(n)了，之所以需要从头开始查找，是因为我们需要得到将被删除的节点的
# 前一个节点。

# 其实这种做法并非是必须的。我们可以很方便地得到要删除的节点的下一个节点。如果我们
# 把下一个节点的内容复制到需要删除的节点上覆盖原有的内容，再把下一个节点删除，就相当于
# 把当前需要删除的节点删除了
# 但是这种思路还有一个问题，如果我们要删除的是尾节点，尾节点就不存在下一个节点的说法。
# 这样的话我们就仍需要从头结点开始，顺序遍历到该节点的前序节点，并完成删除操作。

# 最后要注意的是，如果链表中只有一个节点，而我们又要删除链表的头结点（也是尾节点），
# 那么，此时我们再删除节点之后，还需要把链表的头结点设置为 nullptr。

class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None
    def __repr__(self):
        return '{}->{}'.format(self.value, self.next)

p = ListNode(0)
p.next = ListNode(1)
p.next.next = ListNode(2)
p.next.next.next = ListNode(3)
p.next.next.next.next = ListNode(4)

# 假如我要删除节点值为 3 的那个节点，首先赋值
p.next.next.next.value = p.next.next.next.next.value
# 然后再删除节点值为 3 的那个节点的下一个节点，
# 因为4的下一个节点是尾结点所以将 3 的下一个结点置为 None
p.next.next.next = None

# 假如我要删除节点值为 2 的那个节点，首先赋值
p.next.next.value = p.next.next.next.value
# 然后再删除节点值为 2 的那个节点的下一个节点，
# 因为4的下一个节点是尾结点所以将 2 的下一个结点置为 4 的结点
p.next.next.next = p.next.next.next

class Solution():
    def deleteNodeFromChain(self, pHead, pToBeDeleted):
        # 如果要删除的不是尾结点
        if not pToBeDeleted.next.next == None:
            pToBeDeleted.value = pToBeDeleted.next.value
            pToBeDeleted.next = pToBeDeleted.next.next
        elif pHead == pToBeDeleted:
            # 如果要删除的是头结点（尾结点）
            pHead = None
        else:
            # 如果要删除的是尾结点
            pToBeDeleted.value = pToBeDeleted.next.value
            pToBeDeleted.next = None

# 接下来可以分析这种思路的实现复杂度。对于 n-1 个非尾结点而言，我们可以在 O(1) 时间内
# 把下一个节点的内存复制覆盖要删除的节点，并删除下一个节点；对于尾结点而言，由于仍然
# 需要顺序查找，时间复杂度是 O(n)。因此总的平均时间复杂度是 [(n-1)*O(1) + O(n)]/n
# = O(1) 符合面试官的要求。