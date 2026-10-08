class Solution:
    def ssd(self,n):
        return sum(int(c) ** 2 for c in str(n))

    def isHappy(self, n: int) -> bool:
        seen = set()
        seen.add(n)
        while True :
            n = self.ssd(n)
            if n == 1:
                return True
            if n in seen :
                return False
            seen.add(n)
        