class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            for j in range(i,len(s)):
                temp = s[i:j+1]
                if temp == temp[::-1] and (j+1-i) > len(longest):
                    longest = temp
        return longest                    