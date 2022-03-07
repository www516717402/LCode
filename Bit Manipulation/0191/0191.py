# 和190类似，解码每个二进制位
def func_191(data):
    r = 0
    for i in range(32):
        r += data % 2
        data = data // 2
        if data == 0:
            break
    return r

#  移动掩膜
def hammingWeight(self, n: int) -> int:
    count = 0
    
    mask = 1
    for _ in range(32):
        if n & mask != 0:
            count += 1
        mask = mask << 1
        
    return count
data = 11  # 1011
print(func_191(data))  # 3