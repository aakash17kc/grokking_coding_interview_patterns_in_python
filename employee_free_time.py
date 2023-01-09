
from interval import Interval


def employee_free_time(schedule):
    # Write your code here

    result = []
    meeting_list = []
    for emp in schedule:
        for time in emp:
            meeting_list.append(time)
    meeting_list.sort(key=lambda x: x.start)
    prev_end = meeting_list[0].end

    for i in range(1, len(meeting_list)):
        time = meeting_list[i]
        if time.start > prev_end:
            result.append(Interval(prev_end, time.start))
        prev_end = max(prev_end,time.end)

    return result
