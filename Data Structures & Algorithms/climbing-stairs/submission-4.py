class Solution:

    def f(self,k):
        if k <= 2:
            return k
        if k not in self.stairs :
            self.stairs[k] = self.f(k-1) + self.f(k-2)
        return self.stairs[k]

    def climbStairs(self, n: int) -> int:
        self.stairs = dict()
        self.stairs[1] = 1
        self.stairs[2] = 2
        return self.f(n)
        