def min_window(s, t):
    # your code will replace this placeholder return statement
    tmap = {}
    smap = {}

    for ch in t:
        tmap[ch] = tmap.get(ch, 0) + 1
    current = 0
    required = len(tmap)
    left = 0
    res, res_len = [-1, -1], float("infinity")
    for right in range(len(s)):
        ch = s[right]
        smap[ch] = smap.get(ch, 0) + 1

        if ch in tmap and smap[ch] == tmap[ch]:
            current += 1
        while current == required:
            if right - left + 1 < res_len:
                res = [left, right]
                res_len = right - left + 1
            smap[s[left]] -= 1
            if s[left] in tmap and smap[s[left]] < tmap[s[left]]:
                current -= 1
            left += 1
    left, right = res

    return s[left:right + 1] if res_len != float("infinity") else ""

    pass
