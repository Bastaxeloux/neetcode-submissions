class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2 :
            return n
        else :
            l = [1,2]
            i = 3
            while i <= n:
                temp = l[0] + l[1]
                l[0] = l[1]
                l[1] = temp
                i += 1
        return l[1]