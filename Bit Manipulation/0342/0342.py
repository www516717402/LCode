def fun_342(data):
    if data == 1:
        return True
    while data > 4:
        data = data % 4
        if data == 0:
            return True
    False

def func_2(data):
    return data>0 & (not (data&(data-1))) & (not (data & 0xaaaaaaaa))

data = 2
print(func_2(data))