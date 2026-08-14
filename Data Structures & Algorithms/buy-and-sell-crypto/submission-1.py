class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if sorted(prices,reverse=True) == prices :
            return 0
        max_money = 0
        for i,buy in enumerate(prices):
            for j in range(i+1,len(prices)):
                max_money = max(max_money, prices[j]-buy)
        return max_money