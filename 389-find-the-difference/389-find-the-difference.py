class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in range(len(s)):
            t = t.replace(s[i],'',1)
        return t