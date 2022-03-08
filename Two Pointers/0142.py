# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def func142_s1(node_list):
    index = []
    node = node_list
    while node.next:
        index.append(id(node))
        node = node.next
        if id(node) in index:
            # todo return node
            return index.index(id(node))
    return None

def func142_s2(node_list):
    fast, slow, head = node_list
    while fast and fast.next:
        if fast == slow:
            break
        slow = slow.next
        fast = fast.next.next
    else:
        return None
    while head != slow:
        head = head.next
        slow = slow.next
    return slow


head = ListNode(3)
a = ListNode(2)
head.next = a
b = ListNode(0)
a.next = b
c = ListNode(-4)
b.next = c

c.next = a

print(func142_s1(head))
