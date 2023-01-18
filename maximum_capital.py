import heapq
from heapq import heappush, heappop


def maximum_capital(c, k, capitals, profits):
    min_cap_heap = []
    current_cap = c
    max_profit_heap = []
    for i in range(len(capitals)):
        heappush(min_cap_heap, (capitals[i], i))

    for g in range(k):

        while min_cap_heap and min_cap_heap[0][0] <= current_cap:
            c, i = heappop(min_cap_heap)
            heappush(max_profit_heap, -profits[i], i)
        if not max_profit_heap:
            break
        j = -heappop(max_profit_heap)[0]
        current_cap = current_cap + j
    return current_cap
