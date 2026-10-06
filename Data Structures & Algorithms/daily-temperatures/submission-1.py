class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        out = [0]*n
        for i in range(n-1,-1,-1):
            while (len(stack) != 0) and (temperatures[i] >= temperatures[stack[-1]]):
                stack.pop()
            if len(stack) == 0:
                out[i] = 0
            else :
                out[i] = stack[-1]-i
            stack.append(i)
        print(stack)
        return out