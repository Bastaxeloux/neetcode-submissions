class Solution:
    def twoSum(self,nums,target):
        seen, out = set(), set()
        for num in nums :
            if target-num in seen :
                temp = sorted([num,target-num])
                out.add(tuple(temp))
            else : 
                seen.add(num)
        return out

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        out = []
        for i,num in enumerate(nums) :
            nums_filtered = nums.copy()
            nums_filtered.pop(i)
            if bool(self.twoSum(nums_filtered,-num)) :
                couples = self.twoSum(nums_filtered,-num)
                for c in couples :
                    triplet = sorted(list(c) + [num])
                    triplets.add(tuple(triplet))
        if bool(triplets) :
            out = [list(e) for e in triplets]
        return out