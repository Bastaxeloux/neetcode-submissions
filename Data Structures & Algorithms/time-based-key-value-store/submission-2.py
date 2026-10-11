class TimeMap:
    def __init__(self):
        self.timemap = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timemap :
            self.timemap[key].append((timestamp,value))
        else :
            self.timemap[key] = [(timestamp,value)]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.timemap:
            values = self.timemap[key]
            l,r = 0,len(values)-1
            if values[l][0] > timestamp:
                return ""
            else :
                while l<r:
                    mid = r-(r-l)//2
                    if values[mid][0] > timestamp:
                        r = mid-1
                    else :
                        l = mid
                return values[l][1]
        return ""