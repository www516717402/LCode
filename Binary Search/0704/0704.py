
def func(nums, target):
    length = len(nums)
    for l_id in range(length):
        r_id = length - l_id - 1
        l_value, r_value = nums[l_id], nums[r_id]
        if l_id > r_id or l_value > target:
            return -1
        if l_value == target:
            return l_id
        elif r_value == target:
            return r_id
    return -1


if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(func(nums=nums, target=target))
