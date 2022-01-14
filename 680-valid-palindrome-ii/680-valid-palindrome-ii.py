class Solution:
    def validPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s)-1
        count = 0
        # for i in range(len(s)):
        while start<=end:
            if s[start]==s[end]:

                s = s[start+1:end]
                end-=2
                if len(s)==1 or len(s)==0:
                    return True
            else:

                sub1 = s[1:]
                sub2 = s[:end]
                if sub1==sub1[::-1]:
                    return True
                elif sub2==sub2[::-1]:
                    return True
                else:
                    return False
