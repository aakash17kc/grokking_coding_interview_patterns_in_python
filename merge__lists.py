from typing import Optional, List
from queue import PriorityQueue
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    q = []
    head = point = ListNode(0)
    for i in range(len(list)):
        if lists[i]:
            heapq.heappush(q, (lists[i].val, i, lists[i]))
    heapq.heapify(q)
    while q:
        val, pos, node = heapq.heappop(q)
        point.next = node
        point = point.next
        node = node.next
        if node:
            pos += 1
            heapq.heappush(q, (node.val, pos, node))
