class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = dict()
        l,n = 0,len(s)
        w_max = 0
        for r in range(n):
            count[s[r]] = count.get(s[r],0) + 1
            while (r-l+1) - max(count.values(),default = 0) > k:
                count[s[l]] = count.get(s[l],0) - 1
                l += 1
            w_max = max(w_max,r-l+1)
        return w_max
            
