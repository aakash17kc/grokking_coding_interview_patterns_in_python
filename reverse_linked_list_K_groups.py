def reverse_linked_list_K(head, k):
    if k <= 1 or not head:
        return head
    count = 0
    n = get_length(head)
    prev, curr = None, head

    while True:
        last_of_prev, last_of_curr = prev, curr
        prev, curr, temp = reverse_group(curr,k)
        if last_of_prev:
            last_of_prev.next = prev
        else:
            head = prev
            last_of_curr.next = curr
        if curr is None or  n - count < k:
            break
        prev = last_of_curr
    return head

def get_length(head):
    curr = head
    len = 0
    while curr is not None:
        curr = curr.next
        len += 1
    return len


def reverse_group(head, k):
    prev, curr = None, head
    i = 0
    temp = None
    while curr and i < k:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        i += 1
    return prev, curr, temp
