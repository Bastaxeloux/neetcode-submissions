class Solution:
    def __init__(self):
        self.stairs = dict()
        self.stairs[1] = 1
        self.stairs[2] = 2

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        if n-2 not in self.stairs :
            self.stairs[n-2] = self.climbStairs(n-2)
        if n-1 not in self.stairs :
            self.stairs[n-1] = self.climbStairs(n-1)
        return self.stairs[n-1] + self.stairs[n-2]  