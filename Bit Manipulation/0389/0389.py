def func(a, b):
    r = 0
    for i in (a + b):
        r = ord(i) ^ r
    return chr(r)


a, b = "ba", "cab"
print(func(a, b))
