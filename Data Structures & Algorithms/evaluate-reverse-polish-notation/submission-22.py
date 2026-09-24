class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        to_do = []
        nums = [str(c) for c in range(-200,201)]
        for t in tokens :
            # print(to_do)
            if t in nums :
                to_do.append(int(t))
            else :
                if t == "+":
                    cal = to_do[-2]+to_do[-1]
                if t == "-":
                    cal = to_do[-2]-to_do[-1]
                if t == "*":
                    cal = int(to_do[-2]*to_do[-1])
                if t == "/":
                    cal = int(to_do[-2]/to_do[-1])
                to_do.pop(-1)
                to_do.pop(-1)
                to_do.append(cal)
        return int((10*to_do[0])//10)