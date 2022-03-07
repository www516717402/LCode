def fun_318(data):
    if len(data) < 2:
        return 0
    encode_int = [0] * len(data)
    for i in range(len(data)):
        for c in data[i]:
            encode_int[i] |= 1 << (ord(c) - ord("a"))
    max = 0
    for i in range(len(data)):
        for j in range(i, len(data)):
            if (
                not (encode_int[i] & encode_int[j])
                and len(data[i]) * len(data[j]) > max
            ):
                max = len(data[i]) * len(data[j])
    return max


data = ["a","aa","aaa","aaaa"]
print(fun_318(data))
