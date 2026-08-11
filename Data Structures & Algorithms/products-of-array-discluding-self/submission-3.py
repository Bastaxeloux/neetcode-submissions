class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n,left,right = len(nums),1,1
        output = [1] * n
        for i in range(n):
            output[i] *= left
            left *= nums[i]
            output[n-1-i] *= right
            right *= nums[n-1-i]
        return output