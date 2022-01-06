class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        conversion_dict = dict()
        if len(s)==len(t):
            for i in range(len(s)):
                if not s[i] in conversion_dict:
                    if t[i] not in conversion_dict.values():
                        conversion_dict[s[i]] = t[i]
                    else:
                        return False
                else:
                    if conversion_dict[s[i]] != t[i]:
                        return False
                    else:
                        pass
            return True
        else:
            return False