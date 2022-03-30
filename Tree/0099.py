class TreeNode(object):
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


def func_0099_m1(root):
    def in_order(root):
        if not root:
            return
        yield from in_order(root.left)
        yield from in_order(root.right)
        yield root
    # pre_node = next(root)
    # cur_node = next(root)
    # next_node = next(root)
    swap_node = []
    tmp_node = root
    first_flag = True
    for node in in_order(root):
        if first_flag and tmp_node.val > node.val:
            swap_node.append(tmp_node)
        if not first_flag and first_flag and tmp_node.val > node.val:
            swap_node.append(tmp_node)
        if len(swap_node) == 2:
            swap_node[0].val, swap_node[1].val = (
                swap_node[1].val,
                swap_node[0].val,
            )
            return root
    return root
