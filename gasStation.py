class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # if total gas , total cost -> not possible
        if sum(gas) < sum(cost):
            return -1
        total_gas = 0
        st = 0
        for i in range(len(gas)):
            total_gas += gas[i] - cost[i]
            if total_gas < 0:
                total_gas = 0
                st = i+1
        return st