class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,n = 0,len(s)
        occur = dict()
        cost = 0
        max_l = 0
        for r in range(n):
            occur[s[r]] = occur.get(s[r],0) + 1
            max_value = max(occur.values())
            cost = r-l+1 - max_value
            while cost > k :
                occur[s[l]] = occur.get(s[l],0) - 1
                l += 1
                max_value = max(occur.values())
                cost = r-l+1 - max_value
            max_l = max(max_l,r-l+1)
        return max_l