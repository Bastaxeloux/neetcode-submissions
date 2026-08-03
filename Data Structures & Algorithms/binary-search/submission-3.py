class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a,b = 0,len(nums)-1
        while a<=b:
            print("a=",a," and b=",b)
            m = (b-a)//2+a
            if nums[m] == target :
                return m
            elif nums[m]>target:
                b = m-1
            elif nums[m]<target:
                a = m+1
        return -1