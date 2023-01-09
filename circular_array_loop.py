def next_step(nums, index, curr_dir):
    next_dir = False
    if nums[index] > 0:
        next_dir = True
    else:
        next_dir = False

    if next_dir != curr_dir or nums[index] % len(nums) == 0:
        return -1
    step = index + nums[index]
    return step % len(nums)


def circular_array_loop(nums):
    curr_dir = None
    n = len(nums)
    if n == 0: return False

    for i in range(len(nums)):
        if abs(nums[i]) == n:
            return False
        if nums[i] > 0:
            curr_dir = True
        else:
            curr_dir = False
        slow = i
        fast = i
        while slow != fast or slow == -1 or fast == -1:
            slow = next_step(nums, slow, curr_dir)
            if slow == -1: break
            fast = next_step(nums, fast, curr_dir)
            if fast != -1:
                fast = next_step(nums, fast, curr_dir)
            if fast == -1 or slow == fast:
                break
        if slow == fast:
            return True
    return False

