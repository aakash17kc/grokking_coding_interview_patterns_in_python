from interval import Interval


# Function to find the intersecting points between two intervals
def intervals_intersection(interval_list_a, interval_list_b):
    # TODO: Write your code here
    res = []
    i, j = 0, 0
    while i < len(interval_list_a) and j < len(interval_list_b):
        inta = interval_list_a[i]
        intb = interval_list_b[j]
        start = max(inta.start, intb.start)
        end = min(inta.end, intb.end)
        if start <= end:
            res.append(Interval(start, end))
            if inta.end < intb.end:
                i += 1
            else:
                j += 1
    return res
