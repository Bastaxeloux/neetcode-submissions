class Solution:
    def isPalindrome(self, s: str) -> bool:
        striped_s = [c for c in s.lower() if c.isalnum()]
        return striped_s == striped_s[::-1]