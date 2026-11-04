class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        a,b = nums[0], max(nums[0],nums[1])
        aw,bw = 0, nums[1]
        for i in range(2,n):
            aw,bw = bw,max(bw,aw+nums[i])
            if i != n-1:
                a,b = b,max(b,a+nums[i])
        return max(b,bw)