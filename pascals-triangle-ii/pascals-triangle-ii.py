class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal_tri = [[1],[1,1]]
        if rowIndex == 0:
            return pascal_tri[0]
        elif rowIndex==1:
            return pascal_tri[1]
        else:
            for i in range(2, rowIndex+1):
                temp = [1]
                for x in range(len(pascal_tri[i-1])-1):
                    temp.append(pascal_tri[i-1][x]+pascal_tri[i-1][x+1])
                temp.append(1)
                pascal_tri.append(temp)
            return pascal_tri.pop()
                    