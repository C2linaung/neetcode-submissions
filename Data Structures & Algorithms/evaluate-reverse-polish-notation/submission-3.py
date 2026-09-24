class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = set('+-/*')
        stack = [] # list of strings
        for tok in tokens:
            if tok in op:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                res = 201
                if tok == "+": res = int(num1 + num2)
                if tok == "-": res = int(num1 - num2)
                if tok == "*": res = int(num1 * num2)
                if tok == "/": res = int(num1 / num2)
                stack.append(str(res))
            else:
                stack.append(tok)
        return int(stack[0])