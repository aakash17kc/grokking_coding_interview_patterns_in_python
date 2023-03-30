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