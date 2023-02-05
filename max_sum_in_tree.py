def max_path_sum(self, root):
    self.max_sum = float('-inf')
    self.max_contrib(root)
    return self.max_sum


def max_contrib(self, root):
    if not root:
        return 0
    left_sum = self.max_contrib(root.left)
    right_sum = self.max_contrib(root.right)

    left_tree = 0
    right_tree = 0
    if left_sum > 0:
        left_tree = left_sum
    if right_sum > 0:
        right_tree = right_sum

    sum_val = root.data + left_tree + right_tree
    self.max_sum = max(self.max_sum, sum_val)

    if not root.data:
        return max(left_tree, right_tree)
    else:
        return root.data + max(left_tree, right_tree)
