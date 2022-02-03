class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        print("--------------------------")
        dict_sub = dict()
        for i in s1:
            if i in dict_sub:
                dict_sub[i] +=1
            else:
                dict_sub[i] = 1
        
        n = len(s1)
        for i in range(len(s2)-len(s1)+1):
            substr = s2[i:i+n]
            dict_slider = dict()
            flag = True
            for i in substr:
                if i in dict_slider:
                    dict_slider[i] +=1
                else:
                    dict_slider[i] = 1
                    
            for i, val in dict_sub.items():
                if i not in dict_slider or dict_slider[i]!=val:
                    flag = False
                else:
                    pass
            print("dict_sub: ",dict_sub)
            print("dict_slider: ",dict_slider)
            print("flag: ",flag)
            if flag:
                return True

        return False
                