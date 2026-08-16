class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p, profit_at_p = 0,0
        for i,p in enumerate(prices) :
            profit_at_p = max(prices[i:]) - p
            max_p = max(profit_at_p,max_p)
        return max_p
        