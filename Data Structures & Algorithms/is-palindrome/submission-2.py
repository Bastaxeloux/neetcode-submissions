class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_filtered = [car.lower() for car in s if car.isalnum()]
        print(s_filtered[::-1])

        return s_filtered == s_filtered[::-1]