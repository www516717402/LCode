def InsertSorted(data, reserved=False):
    for i in range(len(data)):
        while i > 0 and (
            (data[i - 1] > data[i] and not reserved)
            or (data[i - 1] < data[i] and reserved)
        ):
            data[i - 1], data[i] = data[i], data[i - 1]
            i -= 1
    return data


def ShellSorted(data, reserved=True):
    length = len(data)
    gap = length // 2
    while gap > 0:
        for idx in range(gap):
            data[idx::gap] = InsertSorted(data[idx::gap], reserved)
        gap = gap // 2
    return data


data = [8, 3, 2, 10, 1, 20, 6, 4, 40]

print(ShellSorted(data, reserved=False))
