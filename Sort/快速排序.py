def QuickSorted(data, reserved=False):
    merge(data)
    return data


def split(data, l_pointer, r_pointer):
    pivot = l_pointer
    high_p = l_pointer
    # step1. 先将销毁
    for i in range(l_pointer + 1, r_pointer + 1):
        if data[i] > data[pivot] and high_p == l_pointer:
            high_p = i
        if data[i] < data[pivot] and high_p > l_pointer:
            swap(data, i, high_p)
            high_p += 1
    high_p -= 1
    if high_p < l_pointer:
        high_p = r_pointer
    swap(data, pivot, high_p)
    return high_p


def merge(data, l_pointer=None, r_pointer=None):
    l_pointer = 0 if l_pointer is None else l_pointer
    r_pointer = len(data) - 1 if r_pointer is None else r_pointer
    if l_pointer < r_pointer:
        partitionIndex = split(data, l_pointer, r_pointer)
        merge(data, l_pointer, partitionIndex - 1)
        merge(data, partitionIndex + 1, r_pointer)


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


data = [8, 16, 24, 6]

print(QuickSorted(data, reserved=True))
