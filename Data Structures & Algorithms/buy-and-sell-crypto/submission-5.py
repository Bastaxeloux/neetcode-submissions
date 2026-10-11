class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i,p in enumerate(prices) :
            profit = max(p - min(prices[:i+1]),profit)
        return profit