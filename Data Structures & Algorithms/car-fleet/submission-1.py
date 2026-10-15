class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        couples = sorted([list(e) for e in zip(position,speed)],reverse=True)
        times = [(target-couples[i][0])/couples[i][1] for i in range(len(speed))]
        ndiff = set()
        maxval = times[0]
        for i,t in enumerate(times) :
            if maxval>times[i]:
                times[i] = maxval
            maxval = max(maxval,times[i])
            ndiff.add(times[i])
        return len(ndiff)