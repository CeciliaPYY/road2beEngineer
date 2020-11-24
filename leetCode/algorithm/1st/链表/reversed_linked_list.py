class LNode:
    def __init__(self, x=None):
        self.data = x
        self.next = None


def reverse1(head):
    """
    就地翻转
    """
    # 1. 首先判断链表是否为空
    if head is None or head.next is None:
        return

    # 2. 对链表首节点做特殊处理
    _cur = head.next  # 首先跳到首节点
    _next = _cur.next  # 记录后集结点
    _cur.next = None  # 将首节点指向None
    pre = _cur  # cur和pre各向后移动一位
    _cur = _next
    # 3. 对链表中间循环处理
    while _cur.next is not None:
        _next = _cur.next
        _cur.next = pre
        pre = _cur
        _cur = _next

    # 4. 对链表最后一个节点做特殊处理
    _cur.next = pre
    head.next = _cur


def reverse_with_no_head(head):
    """
    递归翻转，链表不带头结点
    """
    # 1. 首先判断链表是否为空
    if head is None or head.next is None:
        return head

    new_head = reverse_with_no_head(head.next)
    head.next.next = head  # 将剩余结点翻转
    head.next = None  # 将剩余结点指向None

    return new_head


def reverse2(head):
    """
    递归翻转，链表带头结点
    """
    if head is None:
        return

    cur = head.next
    new = reverse_with_no_head(cur)
    head.next = new
    return new


def reverse3(head):
    """
    插入翻转
    """
    if head is None or head.next is None:
        return

    _cur = head.next.next
    head.next.next = None

    while _cur is not None:
        _next = _cur.next  # 首先先把下一个记下
        _cur.next = head.next  # 换方向
        head.next = _cur  # 把head指向当前这个
        _cur = _next  # 换下一节点


if __name__ == "__main__":
    i = 1
    node = LNode(0)
    node.next = None
    tmp = None
    cur = node
    while i < 8:
        tmp = LNode(i)
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1
    print("逆序前:")
    cur = node.next
    while cur is not None:
        print(cur.data)
        cur = cur.next

    print("逆序后:")
    reverse3(node)
    cur = node.next
    while cur is not None:
        print(cur.data)
        cur = cur.next
