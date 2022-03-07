def func_231(data):
    if data < 1:
        return True
    r = 1
    while r <= data:
        if r == data:
            return True
        r = r << 1
    return False


data = 3

print(func_231(data))
