def CountingSorted(data, reserved=True):
    min_num, max_num = get_min_max(data)
    bucket = [0] * (max_num - min_num + 1)
    for dd in data:
        bucket[dd - min_num] += 1
    total_num = 0
    for k in range(len(bucket)):
        while bucket[k] > 0:
            data[total_num] = k + min_num
            bucket[k] -= 1
            total_num += 1
    return data


def get_min_max(data):
    min_num, max_num = data[0], data[0]
    for k in data:
        if min_num > k:
            min_num = k
        if max_num < k:
            max_num = k
    return min_num, max_num


data = [8, 3, 2, 10]

print(CountingSorted(data, reserved=True))
