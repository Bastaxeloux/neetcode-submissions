class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_filtered = [car.lower() for car in s if car.isalnum()]
        return s_filtered == s_filtered[::-1]