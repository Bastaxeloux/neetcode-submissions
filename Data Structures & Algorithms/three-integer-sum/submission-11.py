class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets, output = set(), []
        nums.sort()
        for i,num in enumerate(nums) :
            l,r = i+1,len(nums)-1
            while l<r:
                threesum = num + nums[l] + nums[r]
                if threesum > 0 :
                    r -= 1
                elif threesum < 0 :
                    l += 1
                else :
                    triplets.add((num,nums[l],nums[r]))
                    r -= 1
                    l += 1
        for triplet in triplets :
            output.append(list(triplet))
        return output