def func(data):
    data = sorted(data)
    return sum(data[::2])

data = [1,2,3,4]
print(func(data))