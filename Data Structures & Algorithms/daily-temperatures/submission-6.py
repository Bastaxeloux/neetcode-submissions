class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n,store = len(temperatures),[]
        out = []
        for i in range(n-1,-1,-1):
            store = [s for s in store if s[0] > temperatures[i]]
            if len(store) != 0:
                temp,idx = store[-1]
                out.append(idx-i)
            else :
                out.append(0)
            store.append((temperatures[i],i))
        out.reverse()
        return out