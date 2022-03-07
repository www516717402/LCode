def add_sum(numbers, target):
    m = dict()
    for i, data in enumerate(numbers):
        if data in m.keys():
            return m[data], i + 1
        m[target - data] = i + 1
    return dict


if __name__ == "__main__":
    print(add_sum([1, 3, 5, 7, 8], 15))
