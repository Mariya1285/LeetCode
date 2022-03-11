class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        new_dict = dict()
        if len(s)!=len(t):
            return False
        for i in s:
            if i in new_dict:
                new_dict[i]+=1
            else:
                new_dict[i]=1
        # print(new_dict)
        for i in t:
            if i in new_dict:
                new_dict[i]-=1
        # print(new_dict.values())
        
        if any(new_dict.values())!=0:
            return False
        return True
        