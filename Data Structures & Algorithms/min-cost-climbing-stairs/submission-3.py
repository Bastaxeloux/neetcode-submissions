class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {0: 0, 1: 0}
        def f(i):
            if i not in memo:
                memo[i] = min(f(i - 1) + cost[i - 1], f(i - 2) + cost[i - 2])
            return memo[i]
        return f(len(cost))