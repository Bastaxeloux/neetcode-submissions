class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        rate_a, rate_b = 1,max(piles)
        while rate_a <= rate_b :
            mid = (rate_b-rate_a)//2+rate_a
            duree = sum(-(-pile//mid) for pile in piles)
            if duree <= h:
                rate_b = mid - 1
            elif duree > h :
                rate_a = mid + 1
        return rate_a