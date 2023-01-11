def first_k_missing_numbers(arr, k):
    index = 0
    n = len(arr)
    while index < len(arr):
        value = arr[index] - 1
        while 1 <= arr[index] <= n and arr[index] != arr[value]:
            arr[index], arr[value] = arr[value], arr[index]
        else:
            index += 1
    res = []
    last_item = 0
    for i in range(len(arr)):
        if i + 1 != arr[i]:
            last_item = i+1
            res.append(i + 1)
    if last_item == 0:
        last_item = max(arr)
    # last_item =0
    # if res:
    #     last_item = max(max(arr), max(res))
    # else: last_item = max(arr)
    while len(res) < k:
        last_item +=1
        res.append(last_item)
    return res[:k]


if __name__ == '__main__':
    print(first_k_missing_numbers(
[-23, -4, -1, -54, -6, -9] , 3))
