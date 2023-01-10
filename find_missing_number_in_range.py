

def find_missing_number(nums):
    n = len(nums)
    ind = 0
    index = 0

    while ind < n:
        ind += 1
        value = nums[index]
        if value < n and value!=nums[value]:
            nums[index], nums[value] = nums[value],nums[index]
        else: index +=1
    for x in range(n):
        if x != nums[x]:
            return x
    return -1