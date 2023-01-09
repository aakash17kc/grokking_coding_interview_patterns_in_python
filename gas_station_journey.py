
def gas_station_journey(gas, cost):
    if sum(gas) < sum(cost):
        return -1

    st = 0
    total_gas = 0
    for i in range(len(gas)):
        total_gas += gas[i] - cost[i]
        if total_gas < 0:
            total_gas = 0
            st += 1
    return st