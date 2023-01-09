import math


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        dpleft = [0] * len(prices)
        dpright = [0] * (len(prices) + 1)
        min_left = prices[0]
        max_right = prices[-1]
        for i in range(1,len(prices)):
            curr = prices[i]
            dpleft[i] = max(dpleft[i - 1], prices[i] - min_left)
            min_left = min(min_left, prices[i])
            r = n - i - 1
            dpright[r] = max(dpright[r + 1], max_right - prices[r])
            max_right = max(max_right, prices[r])
        if 2 * k > n:
            res = 0
            for i, j in zip(prices[1:], prices[:-1]):
                res += max(0, i - j)
                t = math.inf
            return res

        maxP = 0
        for i in range(n):
            maxP = max(maxP, dpleft[i]+ dpright[i + 1])
        return maxP
