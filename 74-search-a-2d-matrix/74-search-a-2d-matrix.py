class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        col = len(matrix[0])
        row = len(matrix)
        
        start = 0
        end = (row*col)-1
        mid = start +((end-start)//2)
        
        while start<=end:
            element = matrix[mid//col][mid%col]
            
            if element==target:
                return True
            elif element<target:
                start = mid+1
            elif element>target:
                end = mid-1
            mid = start+((end-start)//2)
        return False