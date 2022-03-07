def SelectSorted(data, reserved=False):
    for i in range(len(data)):
        idx = i
        for j in range(i, len(data)):
            if (data[i] > data[j] and not reserved) or (
                data[i] < data[j] and reserved
            ):
                idx = j
        if idx != i:
            data[idx], data[i] = data[i], data[idx]
    return data


data = [8, 3, 2, 10]

print(SelectSorted(data, reserved=False))
