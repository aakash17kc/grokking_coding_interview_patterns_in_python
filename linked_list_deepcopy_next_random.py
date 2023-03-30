# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        old = head
        node = Node(old.val,None,None)
        hasht = {}
        hasht[old] = node
        def getClone(node):
            if node:
                if node in hasht:
                    return hasht[node]
                else:
                    hasht[node] = Node(node.val,None,None)
                    return hasht[node]
            return None
        while old:
            node.next = getClone(old.next)
            node.random = getClone(old.random)
            old = old.next
            node = node.next
        return hasht[head]

    def copyRandomListRecursion(self, head: 'Optional[Node]') -> 'Optional[Node]':

        hasht = {}
        def copyRandom(head):
            if not head:
                return None
            if head in hasht:
                return hasht[head]
            new_node = Node(head.val,None,None)
            hasht[head] = new_node
            new_node.next = copyRandom(head.next)
            new_node.random = copyRandom(head.random)
            return new_node

        return copyRandom(head)

