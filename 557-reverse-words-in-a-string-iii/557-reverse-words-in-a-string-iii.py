class Solution:
    def reverseWords(self, s: str) -> str:
        left, right = 0, 0
        temp=""
        while right<=len(s):
            if right==len(s) or s[right] == " ":
                temp+=s[left:right][::-1]
                left=right+1
                if right!=len(s):
                    temp+=" "
            else:
                pass
            right+=1
        return temp