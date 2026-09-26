class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens :
            if t not in "+-/*":
                stack.append(int(t))
            else :
                a = stack.pop()
                b = stack.pop()
                if t == "+":
                    stack.append(b+a)
                if t == "-":
                    stack.append(b-a)
                if t == "*":
                    stack.append(b*a)
                if t == "/":
                    stack.append(int(b/a))
        return stack[0]