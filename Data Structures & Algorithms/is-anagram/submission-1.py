class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sort, t_sort = sorted(s), sorted(t)
        if s_sort == t_sort:
            return True
        return False
        