from _ast import List


class Solution:
    val = 0

    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        self.slices(nums, len(nums) - 1)
        return self.val

    def slices(self, nums, i) -> int:
        if i < 2: return 0
        ap = 0
        if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
            ap = 1 + self.slices(nums, i - 1)
            self.val += ap
        else:
            self.slices(nums, i - 1)
        return ap
