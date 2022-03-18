# base node
class Node:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"Node({self.value})"

    def __iter__(self):
        yield from pre_order(self)
    
    def __len__(self):
        return sum(1 for _ in self)

# Base tree
# display tree
def pre_order(root):
    if root is not None:
        yield root.value
        yield from pre_order(root.left)
        yield from pre_order(root.right)

def in_order(root):
    if root is not None:
        yield from in_order(root.left)
        yield root.value
        yield from in_order(root.right)

def post_order(root):
    if root is not None:
        yield from post_order(root.left)
        yield from post_order(root.right)
        yield root.value

# Base tree
# query node
def query(root, value):
    if root is None:
        return root
    if root.value == value:
        return True
    l_value, r_value = query(root.left), query(root.right)
    return l_value or r_value

# Base tree
# query max
def query_max(root):
    if root is None:
        return root
    def get_max(root, node):
        if root is None:
            return node
        elif root.value > node.value:
            node = root
        l_value = get_max(root.left, node)
        r_value = get_max(root.right, node)
        return l_value if l_value.value>r_value.value else r_value
    return get_max(root, root)

# Base tree
# delete node
# TODO

# binary sort tree
# insert node
def sort_tree_insert(root, value):
    if root is None:
        root = Node(value)
    elif root.value>value:
        root.left = sort_tree_insert(root.left, value)
    else:
        root.right = sort_tree_insert(root.right, value)
    return root

# binary sort tree
# query node
def query(root, value):
    if root is None:
        return False
    if root.value == value:
        return True
    elif value < root.value:
        return query(root.left)
    else:
        return query(root.right)

# binary sort tree
# query max/min
def query_minmax(root, max=True):
    if root is None:
        return root
    # max
    elif max and root.right is None:
        return root
    elif max and root.right is not None:
        return query_minmax(root.right, max)
    # min
    elif not max and root.left is None:
        return root
    else:
        return query_minmax(root.right, max)

# binary sort tree
# delete node
def del_node(root, value):
    if root is None:
        root = None
    elif root.value < value:
        root.right = del_node(root.right, value)
    elif root.value > value:
        root.left = del_node(root.left, value)
    else:
        if root.left is None and root.right is None:
            root = None
        elif root.left and root.right:
            tmp = query_minmax(root.right, max=False)
            root.value = tmp.value
            value = root.value
            root.right = del_node(root.right, value)
        elif root.left is None:
            root = root.right
        else:
            root = root.left
    return root

def is_blance_tree(root):
    
    pass

node1 = Node(0)
node1_left = Node(10)
node1_right = Node(2)
node1.left = node1_left
node1.right = node1_right

for i in node1:
    print(i)
def ppp(node):
    node = 1
    pass
num = 100
ppp(num)
for i in node1:
    print(i)

print("max: ",query_max(node1))
#print(len(node1))