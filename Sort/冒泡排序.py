def BubbleSorted(data, reserved=False):
    for i in range(len(data)):
        for j in range(len(data) - 1):
            if (data[i] < data[j] and not reserved) or (
                data[i] > data[j] and reserved
            ):
                data[i], data[j] = data[j], data[i]
    return data


data = [8, 3, 2, 10]

print(BubbleSorted(data, reserved=True))
