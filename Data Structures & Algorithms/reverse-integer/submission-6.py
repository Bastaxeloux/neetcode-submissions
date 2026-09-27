class Solution:
    def check_range(self,n):
        cond = True
        limit = "2147483647"
        n_srt = str(n)
        for i in range(1,11):
            if int(n_srt[-i]) > int(limit[i-1]):
                return False
            if int(n_srt[-i]) < int(limit[i-1]):
                return True
        return True

    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0 :
            sign = -1
            x = -x
        if len(str(x)) == 10:
            if not self.check_range(x) : 
                return 0
        return sign*int(str(x)[::-1])