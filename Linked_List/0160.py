# TODO not debug 
def func160_s1(linka, linkb):
    # 获取两个链表的长度
    lka, lkb = linka, linkb
    count_a, count_b = 1
    while lka.next:
        lka = lka.next
        count_a += 1
    while lkb:
        lkb = lkb.next
        count_b += 1
    # 最后的节点不相同肯定没有交集
    if lka != lkb:
        return None
    # 差值获取相交的index，找最短的链表进行遍历
    lka, lkb = linka, linkb
    count_a, count_b = 1
    if count_a<count_b:
        target = 2 * count_a - count_b
        while lka.next:
            lka = lka.next
            count_a += 1
            if count_a == target:
                return lka
    else:
        target = 2 * count_b - count_a
        while lkb.next:
            lkb = lkb.next
            count_b += 1
            if count_b == target:
                return lkb
