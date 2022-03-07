def calculate_median(num1, num2):
    is_even = True
    if (len(num1) + len(num2)) % 2:
        is_even = False
    max_range = (len(num1) + len(num2)) // 2 + 1
    result, i, j = 0, 0, 0
    m1_flag, m2_flag = [True, True]
    if len(num1) == 0:
        num1 = [0]
        m1_flag = False
    elif len(num2) == 0:
        num2 = [0]
        m2_flag = False
    print(
        f"is_even={is_even},max_range={max_range},m1_flag={m1_flag},m2_flag={m2_flag}"
    )
    for m in range(max_range):
        v1 = num1[i]
        v2 = num2[j]
        # print(f"i={i},j={j},num1={num1[i]},num2={num2[j]}")
        if m1_flag and v1 < v2 or not m2_flag:
            cur_value = num1[i]
            if i < len(num1) - 1:
                i += 1
            else:
                m1_flag = False
        else:
            cur_value = num2[j]
            if j < len(num2) - 1:
                j += 1
            else:
                m2_flag = False
        if is_even and m == max_range - 2:
            result = cur_value
    if is_even:
        return (result + cur_value) / 2.0
    return cur_value


if __name__ == "__main__":
    nums1 = []
    nums2 = [1, 2, 3]
    print(calculate_median(nums1, nums2))
