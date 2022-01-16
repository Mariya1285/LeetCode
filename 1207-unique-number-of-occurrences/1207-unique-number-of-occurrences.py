class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # print(set(list(dict(Counter(arr)).values())))
        x = list(dict(Counter(arr)).values())
        
        for i in range(len(x)):
            if x[i] not in x[:i]:
                pass
            else:
                return False
            
        return True
        
        
        