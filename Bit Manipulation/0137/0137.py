import copy


def func137(data):
    a, b = 0, 0
    for c in data:
        k = copy.deepcopy(a)
        a = (~a) & (b) & (~c) + (~a) & (b) & (c)
        b = (~k) & (b ^ c)
    return b

data = [0, 0, 3, 0, 4, 3, 3]

print(func137(data))
