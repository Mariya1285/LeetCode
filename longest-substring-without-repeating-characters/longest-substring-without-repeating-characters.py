class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count_list = list()
        for ind,letter in enumerate(s):
            count_unique = 0
            for i in range(ind,len(s)):
                if s[i] not in s[ind:i]:
                    count_unique+=1
                else:
                    break
            print("index: ", ind)
            print("temp: ",count_unique)
            count_list.append(count_unique)
        
        if count_list!=[]:
            print(max(count_list))
            return max(count_list)
        else:
            return 0
            