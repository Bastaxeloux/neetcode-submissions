class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 : return 0
        nums.sort()
        diff = [nums[i]-nums[i-1] for i in range(1,len(nums))]
        diff_filt = [num for num in diff if num!=0]
        n, temp = 0,0
        for i in range(len(diff_filt)):
            if diff_filt[i] == 1:
                temp += 1
            else :
                if temp>n:
                    n = temp
                temp = 0
        if temp > n :
            n = temp
        return n+1