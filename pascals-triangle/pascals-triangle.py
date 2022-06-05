class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        temp = list()
        counter = 1
        for i in range(numRows):
            if i==0:
                temp.append([1])
            elif i==1:
                temp.append([1,1])
            else:
                internal_temp = [1]
                prev_temp = temp[-1]
                temp_length = len(temp[-1])
                for x in range(0,temp_length-1):
                    internal_temp.append(prev_temp[x]+prev_temp[x+1])
                internal_temp.append(1)
                temp.append(internal_temp)
        return temp