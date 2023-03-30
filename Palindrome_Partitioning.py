from typing import List

class Solution:
    def partition(self,s: str,dps) -> List[List[str]]:
        res = []
        l = len(s)
        dp = dps

        def dfs(start, currl, dp):
            if start >= l:
                res.append(currl.copy())
            for end in range(start, l):
                if s[start] == s[end] and (end - start <= 2 or dp[start + 1][end - 1]):
                    dp[start][end] = 1
                    print(dp)
                    currl.append(s[start:end + 1])
                    dfs(end + 1, currl,dp)
                    currl.pop()
        dfs(0,[],dp)
        return res
if __name__ == '__main__':
    df = [[0] * 5] * 5
    dg = [[0] * 5 for _ in range(5)]
    df[0][0] = 1
    print(df)
    # print(dg)
    # print(Solution().partition("abbab",df))
    # print(Solution().partition("abbab",dg))
