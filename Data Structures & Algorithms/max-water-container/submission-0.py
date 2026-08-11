class Solution:
    def maxArea(self, heights: List[int]) -> int:
        volume = 0
        a,b = 0,len(heights)-1
        while a<=b :
            volume = max(volume,(b-a)*min(heights[a],heights[b]))
            #print(f"heights[a]={heights[a]}, heights[b]={heights[b]}, space={b-a}, volume={volume}")
            if heights[a] <= heights[b]:
                a+=1
            elif heights[a] > heights[b]:
                b -= 1
        return volume