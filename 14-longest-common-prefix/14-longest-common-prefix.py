class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or strs[0][i]!=s[i]:
                    return res
            res+=strs[0][i]
        return res
            
        
#         length_list = len(strs)
#         min_len = dict()
#         i = 0
#         min_len[i] = len(strs[i])
#         for ele in strs:
#             if len(ele)<min_len[0]:
#                 min_len[strs.index(ele)]
#         # print(length_list)
        
#         if any([len(ele)==0 for ele in strs]):
#             return str('')
#         else:
#             while i<len(strs[0]):
#                 if  all([ele[i]==strs[0][i] for ele in strs[1:]]):
#                     i+=1
#                 else:
#                     break
#             # print(strs[0][:i])
#             if len(strs[0][:i])==0:
#                 return str('')
#             else:
#                 return strs[0][:i]
            