class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums_set = dict()
        for i,num in enumerate(numbers):
            if target-num in nums_set:
                out = sorted([i+1,nums_set[target-num]])
                return out
            else :
                nums_set[num] = i+1
        return [0,0]