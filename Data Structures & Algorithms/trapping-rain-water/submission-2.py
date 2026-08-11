class Solution:
    def nextWall(self, nums,i):
        indice = i
        tempmax, idmax = 0, i
        while indice < len(nums)-1:
            if nums[indice+1] >= nums[i]:
                return indice+1
            else :
                if nums[indice+1] >= tempmax:
                    tempmax,idmax = nums[indice+1], indice+1
                indice += 1
        return idmax


    def trap(self, height: List[int]) -> int:
        print(self.nextWall([5,0,0],0))
        water = 0
        a,b = 0,0
        while a < len(height)-1 :
            b = self.nextWall(height,a)
            water += (b-a-1)*min(height[a],height[b])-sum(height[a+1:b])
            a = b
        return water