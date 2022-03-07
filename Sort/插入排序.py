def InsertSorted(data, reserved=False):
    for i in range(len(data)):
        while i > 0 and (
            (data[i - 1] > data[i] and not reserved)
            or (data[i - 1] < data[i] and reserved)
        ):
            data[i - 1], data[i] = data[i], data[i - 1]
            i -= 1

    return data


data = [8, 3, 2, 10]

print(InsertSorted(data, reserved=True))
