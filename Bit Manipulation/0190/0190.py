def func_190(data, bits=32):
    r = 0
    for i in range(bits):
        # (data % 2) 有效位，0或1
        # (2 ** (bits - 1 - i))当前位反向之后转换为10进制
        r += (data % 2) * (2 ** (bits - 1 - i))
        # 十进制转二进制
        data = data // 2
        # 转换结束提取退出
        if data == 0:
            break
    return r


data = 13  # ...001011
print(func_190(data, bits=4))  # -> 110100...
