class Solution:
    def twoSum(self,nums,target):
        nums_set = set()
        output = []
        for num in nums:
            if target-num in nums_set:
                output.append([num,target-num])
            else :
                nums_set.add(num)
        return output

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        triplets=set()
        for i,num in enumerate(nums):
            nums_filt = nums.copy()
            nums_filt.pop(i)
            found = self.twoSum(nums_filt,-num)
            if found != []:
                for couple in found:
                    triplet = sorted(couple+[num])
                    triplets.add(tuple(triplet))
        for triplet in triplets :
            output.append(list(triplet))
        return output
        