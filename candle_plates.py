from typing import List


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        nearestLeftCandle = [0] * n
        nearestRightCandle = [0] * n
        plateCount = [0] * n
        res = []
        candle = -1
        count = 0
        for i in range(n):
            k = s[i]
            if k == '|':
                candle = i
            nearestLeftCandle[i] = candle
            if k == '*':
                count += 1
            plateCount[i] = count
        candle = -1
        for i in range(n-1,-1,-1):
            k = s[i]
            if k == '|':
                candle = i
            nearestRightCandle[i] = candle

        for query in queries:
            leftMost = nearestRightCandle[query[0]]
            rightMost = nearestLeftCandle[query[1]]
            if leftMost == -1 or rightMost == -1:
                res.append(0)
            else:
                diff = rightMost - leftMost
                if diff > 1:
                    res.append(plateCount[rightMost] - plateCount[leftMost])
                else:
                    res.append(0)
        return res

if __name__ == '__main__':
    print(Solution().platesBetweenCandles("**|**|***|",[[2,5],[5,9]]))
