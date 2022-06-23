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
            else:
                
                start-=1

        if start==0:
            while s[start]==" ":
                start+=1
            if temp:
                temp+=" "
            else:
                pass
            temp+=s[start:end+1]

            return temp
        return temp
                
            