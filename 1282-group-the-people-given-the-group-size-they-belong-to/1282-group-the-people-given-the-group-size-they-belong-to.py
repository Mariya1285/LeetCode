class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        freq = dict()
        main = list()
        for idx,i in enumerate(groupSizes):
            if i not in freq:
                freq[i] = list([idx])
            else:
                freq[i].append(idx)
                
        for key, val in freq.items():
            temp = list()
            i=0
            for i in range(0,len(val),key):
                main.append(val[i:i+key])
            
                
        return main