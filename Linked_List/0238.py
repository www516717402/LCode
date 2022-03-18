class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def func238_s1(link_list):
    odd_head, odd, even_head, even = link_list, link_list, None, None
    if getattr(link_list, "next", None) is not None:
        even_head, even = link_list.next, link_list.next
    while odd and even and odd.next and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    if even_head is not None:
        odd.next = even_head
    return odd_head

head = ListNode(3)
a = ListNode(2)
head.next = a
b = ListNode(0)
a.next = b
c = ListNode(-4)
b.next = c
d = ListNode(10)
c.next = d

hhh = func238_s1([])
print('...')