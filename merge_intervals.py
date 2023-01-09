from typing import List

from interval import *


def merge_intervals(v: List[Interval]):
    if not v:
        return None
    result = [Interval(v[0].start, v[0].end)]

    for i in range(1, len(v)):
        interval = v[i]
        top_interval = result[-1]
        if top_interval.end >= interval.start:
            top_interval.end = max(top_interval.end, interval.end)
        else:
            result.append(interval)
    return result
