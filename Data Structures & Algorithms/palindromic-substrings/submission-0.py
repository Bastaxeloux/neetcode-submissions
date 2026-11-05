class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(l,r):
            nb = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                nb+= 1
            return nb

        nb = 0
        for i in range(len(s)):
            nb+= expand(i, i)
            nb += expand(i, i + 1)
        return nb
