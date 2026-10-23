class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i,n = 0,len(intervals)
        while i<n and intervals[i][0] < newInterval[0]:
            i+=1
        intervals.insert(i,newInterval)
        out = [intervals[0]]
        for e in intervals[1:]:
            temp = out[-1]
            if temp[1] >= e[0]:
                out.pop()
                out.append([min(e[0],temp[0]),max(e[1],temp[1])])
            else :
                out.append(e)
        return out