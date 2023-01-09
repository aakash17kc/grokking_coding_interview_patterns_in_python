from collections import deque


def find_max_sliding_window(nums, window_size):
    # your code will replace this placeholder return statement

    dq = deque()
    result = []
    for k in range(window_size):
        while dq and nums[k] >= nums[dq[-1]]:
            dq.pop()
        dq.append(k)
    result.append(dq[0])
    for i in range(window_size,len(nums)):
        while dq and nums[i] >= nums[dq[-1]]:
            dq.pop()

        if dq and dq[0] <= i-window_size:
            dq.popleft()
        dq.append(i)
        result.append(dq[0])
    return result

