from heapq import *


def k_smallest_number(lists, k):
    heap = []
    for i in range(len(lists)):
        if not lists[i]:
            continue
        else:
            heappush(heap,(lists[i][0],0,lists[i]))
    count = 0
    item = 0
    while heap:
        item, ind, curr_list = heappop(heap)
        count +=1
        if count == k:
            break
        if ind+1 < len(curr_list):
            heappush(heap,(curr_list[ind+1],ind+1,curr_list))
    return item


