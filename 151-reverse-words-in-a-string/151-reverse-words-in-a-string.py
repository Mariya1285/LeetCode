class Solution:
    def reverseWords(self, s: str) -> str:
        end = len(s)-1
        start = end
        temp = ""
        
        while start>0:
            if s[start]==" ":
                if start!=len(s)-1:
                    if temp:
                        temp+=" "
                        temp += s[start+1:end+1]
                    else:
                        temp += s[start+1:end+1]
                        
                    
                else:
                    pass
                while s[start]==" ":
                    start-=1
                
                end = start
                # print("string captured:", temp)
            else:
                
                start-=1
        print("outside loop:")
        print("start: ", start)
        print("end: ", end)
        print("temp now: ", temp)
        if start==0:
            while s[start]==" ":
                start+=1
            if temp:
                temp+=" "
            else:
                pass
            temp+=s[start:end+1]
            # if temp and temp[len(temp)-1]!=" ":
            #     temp+=" "
            # else:
            #     pass
            # temp+=s[start:end+1]
            # else:
            #     temp+=s[start:end+1]
            return temp
        return temp
                
        #     if start == " " and s[end]!=" ":
        #         temp +=s[start:end+1]
        #         end = start
        #         start-=1
        #     elif s[end]==" " and s[start]!=" ":
        #         end = start
        #         start-=1
        # print(temp)
        
                
            