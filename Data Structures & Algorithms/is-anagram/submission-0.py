class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram = False
        s = sorted(s)
        t = sorted(t)
        if s == t:
            return True
        return False

        