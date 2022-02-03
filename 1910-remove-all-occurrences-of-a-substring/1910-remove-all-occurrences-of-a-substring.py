class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
#         while s.find(part)!=-1:
            
#             s.replace(part,'')
#             print(s)
#         return s
        
    
        # if s.find(part)==-1:
        #     return s
        # return Solution.removeOccurrences(self,s,part)
        
        
#         while len(s)!=0 and s.find(part)!=-1:
#             s = s.replace(part,'')
            
#         return s


        while part in s:
            s = s.replace(part,'',1)
            
            
        return s
    
    
    
    
    