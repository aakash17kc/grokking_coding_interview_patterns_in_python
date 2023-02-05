
from collections import Counter
from heapq import *


def reorganize_string(input_string):
    char_count = Counter(input_string)
    heap = []
    for k, v in char_count.items():
        heap.append((-v, k))
    heapify(heap)
    res = ""
    prev = None
    while len(char_count) > 0 or prev:
        count, char = heappop(heap)
        res = res + char
        count += 1

        if prev:
            heappush(heap, prev)
            prev = None
        if count != 0:
            prev = (count, char)
    return res
