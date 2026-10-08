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
            ssd = self.ssd(n)
            if ssd == 1:
                return True
            if ssd in seen :
                return False
            seen.add(ssd)
            n = ssd
        