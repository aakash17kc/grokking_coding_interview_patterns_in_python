def smallest_missing_positive_integer(nums):
    n = len(nums)
    for i in range(n):
        correct_pos = nums[i] - 1
        while 1 <= nums[i] <= n and nums[i] != nums[correct_pos]:
            nums[correct_pos], nums[i] = nums[i], nums[correct_pos]
            correct_pos = nums[i] - 1
    for i in range(n):
        if i + 1 != nums[i]:
            return i + 1
    return n + 1


if __name__ == '__main__':
    print(smallest_missing_positive_integer([-1, 0, 2, 1, 4]))
