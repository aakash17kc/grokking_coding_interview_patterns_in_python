def backtrack(string, open_count, close, n, res):
    if open_count >= n and close >= n:
        out = str(string)
        replace_str = "[],' "

        for c in replace_str:
            out = out.replace(c, "")
        res.append(out)
        # res.append("".join(string))
    if open_count < n:
        string.append('(')
        backtrack(string, open_count + 1, close, n, res)
        string.pop()
    if close < open_count:
        string.append(')')
        backtrack(string, open_count, close + 1, n, res)
        string.pop()


def generate_paranthesis(n):
    res = []
    backtrack([], 0, 0, n, res)
    # back_track(n, 0, 0, [], res)
    return res


if __name__ == '__main__':
    print(generate_paranthesis(3))
