class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x : x[1])
        j,count = 0,0
        print(intervals)
        for i in range(1,len(intervals)):
            if intervals[j][1] > intervals[i][0]:
                count += 1
            else :
                j=i
        return count