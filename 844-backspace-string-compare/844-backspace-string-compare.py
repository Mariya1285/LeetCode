class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s=list()
        stack_t = list()
        for i in range(max(len(s),len(t))):
            try:
                if s[i]!='#':
                    stack_s.append(s[i])
                else:
                    stack_s.pop()
            except:
                pass
            try:
                if t[i]!='#':
                    stack_t.append(t[i])
                else:
                    stack_t.pop() 
            except:
                pass
        return stack_s==stack_t
        