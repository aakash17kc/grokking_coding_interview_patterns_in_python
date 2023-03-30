def subsets(self, nums: List[int]) -> List[List[int]]:
    n = len(nums)
    res = []
    res.reverse()
    def backtrack(index=0, curr=[]):
        if len(curr) == k:
            res.append(curr[:])
            return
        for i in range(index, len(nums)):
            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()

    for k in range(len(nums) + 1):
        backtrack()
    return res

def wiggle_sort(nums):
    n = len(nums)

    # Find a median.
    mid = sorted(nums)[n // 2]

    # Index-rewiring.
    def A(i):
        return nums[(1 + 2 * i) % (n | 1)]

    # 3-way-partition-to-wiggly in O(n) time with O(1) space.
    i, j, k = 0, 0, n - 1
    while j <= k:
        if A(j) > mid:
            A(i), A(j) = A(j), A(i)
            i += 1
            j += 1
        elif A(j) < mid:
            A(j), A(k) = A(k), A(j)
            k -= 1
        else:
            j += 1