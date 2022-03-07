def MergeSorted(data, reserved=False):
    return split(data, reserved)


def split(data, reserved):
    if len(data) < 2:
        return data
    idx = len(data) // 2
    return merge(
        split(data[:idx], reserved), split(data[idx:], reserved), reserved
    )


def merge(l_data, r_data, reserved):
    result = []
    while l_data and r_data:
        if (l_data[0] > r_data[0] and reserved) or (
            l_data[0] < r_data[0] and not reserved
        ):
            result.append(l_data.pop(0))
        else:
            result.append(r_data.pop(0))
    while l_data:
        result.append(l_data.pop(0))
    while r_data:
        result.append(r_data.pop(0))
    return result


data = [8, 3, 2, 10]

print(MergeSorted(data, reserved=True))
