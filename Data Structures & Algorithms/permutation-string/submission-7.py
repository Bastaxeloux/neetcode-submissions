class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n,m = len(s1),len(s2)
        if n>m :
            return False
        alphabet1, alphabet2 = dict(), dict()
        for i in range(n):
            alphabet1[s1[i]] = alphabet1.get(s1[i],0) + 1
            alphabet2[s2[i]] = alphabet2.get(s2[i],0) + 1
        if alphabet1 == alphabet2 :
                return True
        l,r = 0,n
        while r < m:
            if alphabet2[s2[l]] == 1:
                alphabet2.pop(s2[l])
            else :    
                alphabet2[s2[l]] = alphabet2.get(s2[l],0) - 1
            alphabet2[s2[r]] = alphabet2.get(s2[r],0) + 1
            if alphabet1 == alphabet2 :
                return True
            l += 1
            r += 1
        return False
            
