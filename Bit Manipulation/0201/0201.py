def func_201a(a, b):
    for i in range(a + 1, b + 1):
        a = a & i
    return a


def func_201(a, b):
    bit_shift = 0
    while a < b:
        a = a >> 1
        b = b >> 1
        bit_shift += 1
    return a << bit_shift


