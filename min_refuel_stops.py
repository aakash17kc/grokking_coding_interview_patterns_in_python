def min_refuel_stops(target, start_fuel, stations):
    n = len(stations)
    max_dis  = [0] * (n+1)
    max_dis[0] = start_fuel

    for i in range(n):
        d, fuel = stations[i]
        for j in range(i,-1,-1):
            if max_dis[j] >= d:
                next_dis = max_dis[j] + fuel
                max_dis[j+1] = max(max_dis[j+1],next_dis)
    for i in range(n+1):
        if max_dis[i] >= target:
            return i
    return -1