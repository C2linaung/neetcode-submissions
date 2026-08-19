class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = set("+-/*")
        stack: list[int] = [] 
        def operate(val1: int, val2: int, op: str) -> int:
            if op == "+": return int(val1 + val2)
            if op == "-": return int(val1 - val2)
            if op == "*": return int(val1 * val2)
            if op == "/": return int(val1 / val2)
        
        for t in tokens:
            if t in ops:
                v2 = stack.pop()
                v1 = stack.pop()
                result = operate(v1, v2, t)
                stack.append(int(result))
                continue
            # t is not an operator
            stack.append(int(t))
        return stack[0]