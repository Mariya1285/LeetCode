class Solution:
    def isPalindrome(self, s: str) -> bool:
        y = list(s.lower())
        i = 0
        while i<len(s) and i<len(y):
            if not (y[i].isalpha()or y[i].isnumeric()):
                y.pop(i)
                i-=1
            
            i+=1
        print("trying here")       
#         # new = ('').join(y)
#         start = 0
#         end = len(s)-1
#         x = list(s.lower())
#         while start<=end:
#             temp = x[end]
#             x[end] = x[start]
#             x[start] = temp
            
#             start+=1
#             end-=1
            
#         for i in range(len(y)):
#             if 

        start = 0
        end = len(y)-1
        while start<=end:
            if y[start].lower()!=y[end].lower():
                return False
            start+=1
            end-=1
        return True
            