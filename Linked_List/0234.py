class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# TODO 未完成代码
def func234_s2(link_list):
    head, fast, slow = link_list, link_list, link_list
    # 查找中点和反转前半部分
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    # 比较
    while slow:
        if head.val != slow.val:
            return False
    return True

head = ListNode(3)
a = ListNode(2)
head.next = a
b = ListNode(0)
a.next = b
c = ListNode(10)
b.next = c
d = ListNode(20)
c.next = d

print(func234_s2(head))
