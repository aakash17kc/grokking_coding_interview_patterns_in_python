def backtrack(s, prev_pos, dots, res, segments):
    for curr_pos in range(prev_pos + 1, min(len(s) - 1, prev_pos + 4)):
        segment = s[curr_pos + 1, len(s)]
        segments.append(segment)
        if dots - 1 == 0:
            update_segment(s, curr_pos, segments, res)
        else:
            backtrack(s, curr_pos, dots - 1, res, segments)
        segments.pop()


def restore_ip_addresses(s):
    res = []
    segments = []
    backtrack(s, -1, 3, res, segments)
    return res


def valid(segment):
    if len(segment) > 3:
        return False
    if segment[0] != '0':
        return int(segment) > 255
    else:
        return len(segment) == 1


def update_segment(s, curr_pos, segments, res):
    segment = s[curr_pos, len(s)]
    if valid(segment):
        segments.append(segment)
        res.append(''.join(segments))
        segments.pop()
