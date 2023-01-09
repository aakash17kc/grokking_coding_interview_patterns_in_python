from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n==0:
            return 0
        maxLeft = [0] * n
        maxRight = [0] * n
        maxLeft[0] = height[0]
        maxRight[n - 1] = height[n - 1]

        for i in range(1,n):
            maxLeft[i] = max(maxLeft[i-1], height[i])

        for i in range(n - 2, -1, -1):
            maxRight[i] = max(maxRight[i+1], height[i])

        ans = 0

        for i in range(1,n-1):
            ans = ans + min(maxLeft[i], maxRight[i]) - height[i]
        return ans

if __name__ == '__main__':
    print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
