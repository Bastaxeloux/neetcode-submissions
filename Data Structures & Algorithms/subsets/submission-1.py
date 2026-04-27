def subsets_of_size(nums,i):
    n = len(nums)
    subsets_of_size_i = []
    if i == 1:
        for num in nums :
            subsets_of_size_i.append([num])
    elif 1<i<=n: # pour les subsets de taille 2 à n
        for j,num in enumerate(nums[0:n-i+1]): # on stop à n-i
            temp = subsets_of_size(nums[j+1:],i-1)
            for subs in temp:
                subsets_of_size_i.append(subs + [num])
    return subsets_of_size_i 

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        subsets.append([])
        n = len(nums)
        if n == 0 :
            return []
        for i in range (1,n+1):
            # goal is to find all subsets of size i here
            subsets.extend(subsets_of_size(nums,i))
            print(subsets)
        return subsets
