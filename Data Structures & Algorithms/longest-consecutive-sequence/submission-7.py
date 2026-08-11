class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 : return 0
        nums.sort()
        diff = [nums[i]-nums[i-1] for i in range(1,len(nums)) if nums[i]-nums[i-1]!=0 ]
        n, temp = 0,0
        for i in range(len(diff)):
            if diff[i] == 1:
                temp += 1
            else :
                n = max(n,temp)
                temp = 0
        n = max(n,temp)
        return n+1