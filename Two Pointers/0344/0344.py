def func(target):
    l_point = 0
    r_point = len(target) - 1
    while l_point < r_point:
        target[l_point], target[r_point] = target[r_point], target[l_point]
        l_point += 1
        r_point -= 1
    return target


if __name__ == "__main__":
    s = ["h", "e", "l", "l", "o"]
    print(func(s))
