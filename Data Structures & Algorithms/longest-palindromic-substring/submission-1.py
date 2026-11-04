class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r - 1

        best_l, best_r = 0, 0
        for i in range(len(s)):
            for l, r in (expand(i, i), expand(i, i + 1)):
                if r - l > best_r - best_l:
                    best_l, best_r = l, r
        return s[best_l:best_r + 1]