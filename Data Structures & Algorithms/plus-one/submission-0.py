class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = str()
        for c in digits:
            n += str(c)
        n = str(int(n) + 1)
        return([int(c) for c in n])