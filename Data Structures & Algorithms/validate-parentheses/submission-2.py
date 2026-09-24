class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_set = set("({[")

        for c in s:
            if c in open_set:
                stack.append(c)
            else:
                if not stack:
                    return False
                popped = stack.pop()
                if not (
                    (c == ')' and popped == '(') or
                    (c == '}' and popped == '{') or
                    (c == ']' and popped == '[')
                ):
                    return False

        return not stack