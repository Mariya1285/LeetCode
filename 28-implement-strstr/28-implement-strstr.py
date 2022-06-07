class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)>len(haystack):
            return -1
        else:
            print("I am here")
            for ind in range(len(haystack)-len(needle)+1):
                flag = True
                # if len(needle)>1:
                #     if haystack[ind] == needle[0] and haystack[ind+1]==needle[1]:
                #         counter = len(needle)-2
                #         internal_ind = ind+1
                #         while counter>0:
                #             if haystack[internal_ind+1] == needle[counter]:
                #                 counter+=1
                #             else:
                #                 flag = False
                #                 break
                #         if flag == True:
                #             return ind
                # else:
                #     if haystack[ind] == needle[0]:
                #         return ind
                if haystack[ind] == needle[0]:
                    for i in range(1,len(needle)):
                        if haystack[ind+i] != needle[i]:
                            flag = False
                            break
                    if flag == True:
                        return ind
                    
            return -1
                        
                    
                