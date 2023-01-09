from binary_search import binary_search


def find_closest_elements(nums, k, num):
    if len(nums) == k:
        return nums
    left = binary_search(nums, num) - 1
    right = left + 1
    while right - left - 1 < k:
        if left == -1:
            right += 1

        if right == len(nums) or abs(nums[left] - num) <= abs(nums[right] - num):
            left -= 1
        else:
            right += 1
    return nums[left + 1:right]
