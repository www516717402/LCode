def func(nums, target):
    l_flag = True
    if nums[0] == target:
        return 0
    elif nums[0] > target:
        l_flag = False
    for i in range(len(nums)):
        if l_flag:
            if nums[i]==target:
                return i
            elif nums[i]<target:
                return -1
        else:
            if nums[i]==target:
                return i
            elif nums[i]>target:
                return -1
    return -1
    

if __name__ == '__main__':
    
    func()
    