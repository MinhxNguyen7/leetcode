class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        n = len(gas)
        net_costs = [g - c for g, c in zip(gas, cost)]
        if sum(net_costs) < 0: return -1

        start = 0
        tank = 0
        for idx, net_cost in enumerate(net_costs):
            tank += net_cost
            if tank < 0:
                start = idx + 1
                tank = 0

        return start if start < n else -1
                
if __name__ == '__main__':
    print(Solution().canCompleteCircuit(
        [5,1,2,3,4],
        [4,4,1,5,1]
    ))