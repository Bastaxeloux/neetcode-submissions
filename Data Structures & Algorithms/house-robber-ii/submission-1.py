class Solution:
    def rob1(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 :
            return nums[0]
        a,b = nums[0],max(nums[0],nums[1])
        for i in range(2,n):
            a,b = b,max(b,a+nums[i])
        return b
        
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 :
            return nums[0]
        return max(self.rob1(nums[1:]),self.rob1(nums[:-1]))