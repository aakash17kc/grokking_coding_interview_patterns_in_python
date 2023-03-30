class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def maxSum(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            left = maxSum(root.left)
            right = maxSum(root.right)
            if left < 0:
                left = 0
            if right < 0:
                right = 0
            curr_sum = root.val + left + right
            max_sum = max(max_sum, curr_sum)

            if not root.val:
                return max(left, right)
            else:
                return root.val + max(left, right)

        max_sum = float('-inf')
        maxSum(root)
        return max_sum