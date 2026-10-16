class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n,store = len(temperatures),[]
        out = [0]*n
        for i in range(n-1,-1,-1):
            store = [s for s in store if s[0] > temperatures[i]]
            if store:
                temp,idx = store[-1]
                out[i] = (idx-i)
            store.append((temperatures[i],i))
        return out
            
