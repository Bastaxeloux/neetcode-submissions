class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # min cost to reach step i = min (
        #          min_cost reach i-1 + cost[i-1],
        #          min_cost reach i-2 + cost[i-2])
        reach = [0,0]
        n = len(cost)
        for i in range(2,n+1):
            cost_a = reach[i-2] + cost[i-2]
            cost_b = reach[i-1] + cost[i-1]
            reach.append(min(cost_a,cost_b))
            print(f"cost_a={cost_a}, cost_b={cost_b}")
            print(f"reach={reach}")
        return reach[-1]