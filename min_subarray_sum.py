import math


def min_sub_array_len(target, nums):
    # your code will replace this placeholder return statement
    window_len = math.inf
    start = 0
    total_sum = 0
    for i in range(len(nums)):
        total_sum = total_sum + nums[i]
        while total_sum >=target:
            window_len = min(window_len, i-start +1)
            total_sum = total_sum - nums[start]
            start +=1
    return window_len

if __name__ == '__main__':
    print(min_sub_array_len(7,[2, 3, 1, 2, 4, 3]))