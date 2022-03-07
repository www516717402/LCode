def func136(data):
    r = 0
    for d in data:
        r ^= d
    return r;

data = [1,4,1,5,5,4,10,6,10]
print(func136(data))