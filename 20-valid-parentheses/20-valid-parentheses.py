class Solution:
    def isValid(self, s: str) -> bool:
        open_paranthesis = ['(','[','{']
        closed_paranthesis = [')',']','}']
        stack = []
        for ch in s:
            if ch in closed_paranthesis:
                if stack and open_paranthesis[closed_paranthesis.index(ch)]==stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        
        if stack:
            return False
        return True