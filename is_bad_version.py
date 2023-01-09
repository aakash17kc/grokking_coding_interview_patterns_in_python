from api import *

version_api = api(0)


def is_bad_version(v):
    return version_api.is_bad(v)


def first_bad_version(n):
    # -- DO NOT CHANGE THIS SECTION
    version_api.n = n
    low = 1
    high = len(n) - 1
    count = 0

    while low < high:
        mid = low + ((high - low) // 2)
        bad = is_bad_version(n[mid])
        count +=1
        if bad:
            high = mid
        else:
            low = mid + 1
    return low, count



    # --

    # Write your code here:
    return 0, 0
