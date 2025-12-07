def mzero(nums):
    index = 0
    for i in range(len(nums)):
        if nums[i] != 0: 
            nums[index] = nums[i]
            index += 1
    for i in range (index,len(nums)):
        nums[i] = 0
    return nums
nums = [1,2,0,5,0,4,0,8]
a = mzero(nums)
print(a)
