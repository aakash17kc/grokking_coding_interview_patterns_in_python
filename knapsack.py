
def find_max_knapsack_profit(capacity,weights,values):
    if capacity <= 0 or len(values) == 0 or len(weights) != len(values):
        return 0
    profit = [0] * (capacity + 1)
    for i in range(len(values)):
    for c in range(capacity,-1,-1):
        if weights[i] <= c:
            new_profit = profit[c-weights[i]] + values[i]
            profit[c] = max(profit[c],new_profit)
    return profit[capacity]