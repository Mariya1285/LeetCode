class Solution:
    def reverseWords(self, s: str) -> str:
        left, right = 0, 0
        temp=""
        while right<=len(s):
            if right==len(s) or s[right] == " ":
                new_r = right
                new_l = left
                while new_r>new_l:
                    temp+=s[new_r-1]
                    new_r-=1
                # temp+=s[left:right][::-1]
                left=right+1
                if right!=len(s):
                    temp+=" "
            else:
                pass
            right+=1
        return temp