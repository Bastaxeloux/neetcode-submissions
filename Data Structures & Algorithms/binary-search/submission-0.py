class Solution:
    def search(self, nums: List[int], target: int) -> int:
        found=-1
        for i in range(len(nums)):
            if nums[i]==target:
                found=i
        return found