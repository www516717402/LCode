def func(a, b):
    while b:
        a, b = a ^ b, (a & b) << 1
    return a


a, b = 15, 11
print(func(a, b))
