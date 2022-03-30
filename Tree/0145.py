from re import X


class TreeNode(object):
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


def inorderTraversal(root):
    def in_order(root):
        if not root:
            return
        yield from in_order(root.left)
        yield from in_order(root.right)
        yield root.val

    return [i for i in in_order(root)]


a = TreeNode(1)
a.right = TreeNode(2)
a.right.left = TreeNode(3)

print(inorderTraversal(a))
