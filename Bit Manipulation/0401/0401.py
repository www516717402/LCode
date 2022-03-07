# 输入int，输出表示的二进制1的个数
def cal_bits(inter):
    c = 0
    while inter:
        if inter % 2 == 1:
            c += 1
        inter //= 2
    return c


# 每减一次1和按位与操作，就表示最低位的一个1被去除
def cal_bits2(inter):
    c = 0
    while inter:
        inter &= inter - 1
        c += 1
    return c


def func(data):
    result= []
    for h in range(12):
        for m in range(24):
            if (cal_bits(h) + cal_bits(m)) == data:
                result.append(f'{h}'+":"+f'{m}'.rjust(2,"0"))
                pass
    return result


data = 2
print(func(data))
