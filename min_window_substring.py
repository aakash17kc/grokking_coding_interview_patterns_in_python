import math


def minWindow(s: str, t: str) -> str:
    res = [-1, -1]
    min_len = math.inf
    m = len(s)
    n = len(t)

    if m < n:
        return ""
    s_count = {}
    r_count = {}
    for i in range(n):
        r_count[t[i]] = 1 + r_count.get(t[i], 0)

    left = 0
    required = len(r_count)
    current = 0
    for right in range(m):
        s_count[s[right]] = 1 + s_count.get(s[right], 0)

        if s[right] in r_count and r_count[s[right]] == s_count[s[right]]:
            current += 1

        while current == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                res = [left, right]

            s_count[s[left]] -= 1
            if s[left] in r_count and s_count[s[left]] < r_count[s[left]]:
                current -= 1
            left += 1
    return s[res[0]:res[1] + 1] if min_len != math.inf else ""

if __name__ == '__main__':
    print(minWindow("bbaa","aba"))
