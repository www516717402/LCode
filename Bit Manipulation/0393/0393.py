def func(data):
    ct = 0
    for d in data:
        if ct == 0:
            if (d >> 5) == 0b110:
                ct = 1
            if d>>4 == 0b1110:
                ct = 2
            elif d>>3 == 0b11110:
                ct = 3
            elif d >> 7:
                return False
        else:
            if (d >> 6) != 0b10:
                return False
            ct -= 1
    return ct == 0


data = [235, 140, 4]
print(func(data))
