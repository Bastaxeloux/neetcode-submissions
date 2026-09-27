class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for i,n in enumerate(nums):
            if target-n not in diff :
                diff[n]=i
            else :
                return sorted([i,diff[target-n]])
        