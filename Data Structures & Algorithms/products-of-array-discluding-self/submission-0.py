class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zero_count = nums.count(0)
        if zero_count >= 2:
            return [0] * n

        total = 1
        for num in nums:
            if num != 0:
                total *= num

        if zero_count == 1 :
            return [total if num == 0 else 0 for num in nums]

        return [total//num for num in nums]

        