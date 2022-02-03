class Solution:
    def removeDuplicates(self, s: str) -> str:
        left = 0
        right = 1
        while left<len(s)-1 and len(s)>1:

            if s[left]==s[right]:
                s=s[:left]+ s[right+1:]
                if left!=0:
                    left-=1
                    right-=1
            else:
                left+=1
                right+=1
                
        return s