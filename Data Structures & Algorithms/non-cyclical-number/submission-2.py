class Solution:
    def ssd(self,n):
        temp=str(n)
        tot = 0
        for i in range(len(temp)):
            tot += int(temp[i])**2
        return tot

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
        