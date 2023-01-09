import math


def min_window(s, t):
    # your code will replace this placeholder return statement
    if t == "":
        return ""
    n1 = len(s)
    n2 = len(t)
    count_map = {}
    window_map = {}
    left, right = 0, 0
    curr, required = 0, n2
    res_len = math.inf
    res = [-1, -1]
    for i in range(n2):
        count_map[t[i]] = count_map.get(t[i], 0) + 1
    for right in range(n1):
        ch = s[right]
        window_map[ch] = window_map.get(ch, 0) + 1
        if ch in count_map and window_map[ch] == count_map[ch]:
            curr += 1
        while curr == required:
            if right - left + 1 < res_len:
                res_len = right - left + 1
                res = [left, right]

            window_map[ch] -= 1
            if s[left] in count_map and window_map[s[left]] < count_map[s[left]]:
                curr -= 1
            left = left + 1
    return s[res[0]:res[1] + 1] if res_len != math.inf else ""

if __name__ == '__main__':
    min_window("cabwefgewcwaefgcf","cae")
