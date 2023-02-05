from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    res = []
    curr = 0
    generate_per(nums, 0, res)
    return list(res)


def generate_per(nums, curr, res):
    if curr == len(nums) - 1:
        res.append(nums)
        return
    for i in range(curr, len(nums)):
        nums_copy = nums.copy()
        nums_copy[i],nums_copy[curr] = nums_copy[curr],nums_copy[i]
        generate_per(nums_copy, curr + 1, res)


if __name__ == '__main__':
    # print(median_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))
    # print(permute([1, 2, 3]))
    matrix =[1,2,3]
    print(matrix.reverse())