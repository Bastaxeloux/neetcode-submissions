class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = set()
        l,n = 0,len(s)
        maxw = 0
        for r in range(n):
            while s[r] in count :
                count.remove(s[l])
                l+=1
            count.add(s[r])
            maxw = max(maxw,r-l+1)
        return maxw