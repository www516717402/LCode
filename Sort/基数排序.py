def BucketSorted(data, reserved=True):
    n = len(str(max(data)))
    for k in range(n):
        bucket_list = [[] for i in range(10)]
        for i in data:
            # 按第k位放入到桶中
            bucket_list[i // (10 ** k) % 10].append(i)
        data = [j for i in bucket_list for j in i]
    return data


data = [99, 60, 90, 80, 66]

print(BucketSorted(data, reserved=True))
