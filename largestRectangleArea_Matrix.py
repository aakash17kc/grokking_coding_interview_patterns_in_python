from typing import List


def maximalRectangle(self, matrix: List[List[str]]) -> int:
    if not matrix: return 0
    max_a = -1
    dp = [0] * len(matrix[0])
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            dp[j] = dp[j] + 1 if matrix[i][j] == '1' else 0
        max_a = max(max_a, self.largestRectangleArea(dp))
    return max_a


def largestRectangleArea(self, heights: List[int]) -> int:
    stack = [-1]
    n = len(heights)
    max_a = -1
    for i in range(n):
        while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
            curr_h = heights[stack.pop()]
            curr_w = i - stack[-1] - 1
            max_a = max(max_a, curr_h * curr_w)
        stack.append(i)
    while stack[-1] != -1:
        curr_h = heights[stack.pop()]
        curr_w = n - stack[-1] - 1
        max_a = max(max_a, curr_h * curr_w)
    return max_a