class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        a,b = 1,max(piles)
        out = 0
        while a <= b :
            rate = a + (b-a)//2
            temp = [-(-p//rate) for p in piles]
            time = sum(temp)
            if time > h:
                a = rate + 1
            elif time <= h :
                b = rate - 1
                out = rate
        return out