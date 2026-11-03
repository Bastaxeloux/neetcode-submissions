class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a,b,n = 0,0, len(cost)
        for i in range(2,n+1):
            a,b = b, min(a + cost[i-2],b + cost[i-1])
        return b