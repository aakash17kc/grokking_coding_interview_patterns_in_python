from heapq import heappop, heappush, heapify

#https://www.educative.io/courses/grokking-coding-interview-patterns-python/Y5xJqZBQ11n

def median_sliding_window(nums, k):
    # Will store the medians
    medians = []

    # outgoing_num will keep track of invalid numbers that are removed from the window
    outgoing_num = {}

    # max heap
    small_list = []
    heapify(small_list)

    # min heap
    large_list = []
    heapify(large_list)

    # Index of current incoming element being processed
    i = 0

    # Initialize the small_list heap
    # Multiplying each element by -1 to implement max heap.
    for i in range(0, k):
        heappush(small_list, -1 * nums[i])

    # incrementing i by 1 to make it equal to the length of the window
    i += 1

    # transferring the largest 50% of the values from small_list to large_list
    # restoring the sign of each element as we do so
    for j in range(0, k//2):
        element = heappop(small_list)
        heappush(large_list, -1 * element)

    # Start an infinite loop
    while True:
        # Check if the window length is odd
        if (k & 1) == 1:
            medians.append(float(small_list[0] * -1))

        else:
            temp = (float(small_list[0] * -1) + float(large_list[0])) * 0.5
            medians.append(temp)

        # Break the loop if all of the elements are processed
        if i >= len(nums):
            break

        # Outgoing element
        out_num = nums[i - k]

        # Incoming element
        in_num = nums[i]
        i += 1

        # Balance factor
        balance = 0

        # Number `out_num` exits window
        if out_num <= (small_list[0] * -1):
            balance -= 1
        else:
            balance += 1

        # If the outgoing element is not present in the outgoing_num
        # store the `out_num` in the outgoing_num with value 1,
        # otherwise increment the count of `out_num` in the outgoing_num.

        if out_num in outgoing_num:
            outgoing_num[out_num] = outgoing_num[out_num] + 1
        else:
            outgoing_num[out_num] = 1

        # number `in_num` enters window
        if small_list and in_num <= (small_list[0] * -1):
            balance += 1
            heappush(small_list, in_num * -1)
        else:
            balance -= 1
            heappush(large_list, in_num)

        # Re-balance small_list
        if balance < 0:
            heappush(small_list, (-1 * large_list[0]))
            heappop(large_list)
            balance += 1

        # Re-balance large_list
        if balance > 0:
            heappush(large_list, (-1 * small_list[0]))
            heappop(small_list)
            balance -= 1

        # Remove invalid numbers that should be discarded from small_list heap tops
        while (small_list[0] * -1) in outgoing_num and (outgoing_num[(small_list[0] * -1)] > 0):
            outgoing_num[small_list[0] * -1] = outgoing_num[small_list[0] * -1] - 1
            heappop(small_list)

        # Remove invalid numbers that should be discarded from large_list heap tops
        while large_list and large_list[0] in outgoing_num and (outgoing_num[large_list[0]] > 0):
            outgoing_num[large_list[0]] = outgoing_num[large_list[0]] - 1
            heappop(large_list)

    # Return medians
    return medians

if __name__ == '__main__':
    print(median_sliding_window([1,3,-1,-3,5,3,6,7] , 3))
