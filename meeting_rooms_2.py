from interval import Interval


def find_sets(intervals):
    # your code will replace this placeholder return statement
    queue = []
    intervals.sort(key=lambda x: x.start)
    queue.append(intervals[0].end)
    for i in range(1, len(intervals)):
        curr_interval = intervals[i]
        if curr_interval.start > queue[-1]:
            queue.append(curr_interval.end)
    return len(queue)
