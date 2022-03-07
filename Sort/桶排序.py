from math import ceil


def BucketSorted(data, reserved=True):
    min_num, max_num = get_min_max(data)
    bucket_num = ceil((max_num - min_num) / 10)
    bucket_array = [[] for _ in range(bucket_num)]
    for dd in data:
        bucket_array[(dd - min_num) // 10].append(dd)
    result = []
    for bb in bucket_array:
        result += sorted(bb)
    return result


def get_min_max(data):
    min_num, max_num = data[0], data[0]
    for k in data:
        if min_num > k:
            min_num = k
        if max_num < k:
            max_num = k
    return min_num, max_num


data = [99, 60, 90, 80, 66]

print(BucketSorted(data, reserved=True))
