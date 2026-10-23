class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort()
        out = [intervals[0]]
        for e in intervals[1:]:
            temp = out[-1]
            if temp[1] >= e[0]:
                out.pop()
                out.append([min(e[0],temp[0]),max(e[1],temp[1])])
            else :
                out.append(e)
        return out