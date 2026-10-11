class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit,min_buy = 0,prices[0]
        for i,p in enumerate(prices) :
            min_buy = min(min_buy,p)
            profit = max(p-min_buy,profit)
        return profit