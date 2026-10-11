class TimeMap:
    def __init__(self):
        self.timemap = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timemap :
            self.timemap[key].append((timestamp,value))
        else :
            self.timemap[key] = [(timestamp,value)]

    def get(self, key: str, timestamp: int) -> str:
        values = self.timemap.get(key, [])
        res = ""
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            if values[mid][0] <= timestamp:
                res = values[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return res