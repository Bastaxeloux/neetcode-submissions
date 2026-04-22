class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a,b = 0,len(nums)-1
        notfound = -1
        while a<=b :
            mid_idx = (a+b)//2
            if nums[mid_idx] < target :
                a=mid_idx+1
            elif nums[mid_idx] > target :
                b=mid_idx-1
            elif nums[mid_idx] == target:
                return mid_idx
        return notfound