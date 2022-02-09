class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rowStart, rowEnd = 0, len(matrix)-1
        colStart, colEnd = 0, len(matrix[0])-1
        ans = []
        while rowStart<=rowEnd and colStart<=colEnd:
            for i in range(colStart, colEnd+1):
                ans.append(matrix[rowStart][i])
            for i in range(rowStart+1, rowEnd+1):
                ans.append(matrix[i][colEnd])
            for i in range(colEnd-1, colStart-1, -1):
                if rowEnd>rowStart:
                    ans.append(matrix[rowEnd][i])
            for i in range(rowEnd-1, rowStart, -1):
                if colEnd>colStart:
                    ans.append(matrix[i][colStart])
            rowStart += 1
            rowEnd -= 1
            colStart += 1
            colEnd -= 1 
        return ans