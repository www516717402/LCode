def HeapSorted(data, reserved=False):
    # build whole head struct
    for i in range(len(data), -1, -1):
        build_single_heat(data, len(data), i)

    for i in range(1, len(data)):
        build_single_heat(data, len(data), i, base_index=i)

    return data


def build_single_heat(data, max_length, index, base_index=0):
    l_pointer = 2 * (index - base_index) + 1 + base_index
    r_pointer = 2 * (index - base_index) + 2 + base_index
    exchanege_index = index
    if l_pointer < max_length and data[l_pointer] > data[exchanege_index]:
        exchanege_index = l_pointer
    if r_pointer < max_length and data[r_pointer] > data[exchanege_index]:
        exchanege_index = r_pointer
    if exchanege_index != index:
        swap(data, index, exchanege_index)
        build_single_heat(data, max_length, exchanege_index)


def swap(data, i, j):
    data[i], data[j] = data[j], data[i]
    pass


# Driver code to test above
data = [1, 11, 13, 5, 6, 24]

print(HeapSorted(data))
