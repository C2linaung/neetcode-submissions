class Solution:
    def checkValidString(self, s: str) -> bool:
        os = []
        ss = []
        for i, c in enumerate(s):
            if c == "*":
                ss.append(i)
            elif c == "(":
                os.append(i)
            else:
                if os:
                    os.pop()
                else:
                    if not ss:
                        return False
                    ss.pop()
        while os:
            if not ss or ss[-1] < os[-1]:
                return False
            os.pop()
            ss.pop()
        return True