from binary_search import binary_search


def single_non_duplicate(nums):
    # Write your code here to find the single element in a sorted array.

    # You may use the code template provided in the binary_search.py file.
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + ((right - left) // 2)
        if mid % 2 != 0:
            mid -= 1
        if nums[mid] == nums[mid + 1]:
            left = mid + 2
        else:
            right = mid
    return left
