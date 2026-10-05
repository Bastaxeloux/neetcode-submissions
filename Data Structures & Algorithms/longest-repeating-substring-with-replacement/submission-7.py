class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,n,cost,max_l = 0,len(s),0,0
        occur = dict()
        for r in range(n):
            occur[s[r]] = occur.get(s[r],0) + 1
            while (r-l+1) - max(occur.values()) > k:
                occur[s[l]] -= 1
                l += 1
            max_l = max(max_l,r-l+1)
        return max_l