class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        count = 0
        new = ''
        goal_str = ''
        if (len(s) != len(goal)) or len(s)==1:
            return False
        else:
            for i in range(len(s)):
                if s[i]!=goal[i]:
                    count+=1
                    new+=s[i]
                    goal_str+=goal[i]
                else:
                    pass
                    
            if count==2:
                if new[::-1]==goal_str:
                    return True
                else:
                    return False
            elif count==0:
                temp = dict(Counter(s))
                # if any(temp.values)>=2:
                if any(v >= 2 for v in temp.values()):
                    return True
                else:
                    return False
                # if s==goal:
                #     return True
            else:
                return False