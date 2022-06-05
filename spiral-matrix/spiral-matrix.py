class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        temp = list()
        columns = len(matrix[0])
        last_column = columns-1
        rows = len(matrix)
        start_row = 0
        #col_end_right = len(matrix)-1
        first_down = 1
        last_row = rows-1
        first_col = 0
        m = rows     
        n = columns
        while len(temp)<m*n:
            print(first_col,last_column,"sdhsh")
            if first_col==last_column:
                
                temp.extend([s[first_col] for s in matrix[start_row:last_row+1]])
            else:
                
                for i in range(first_col, columns):
                    temp.append(matrix[start_row][i])
                print(temp,1)
                for i in range(first_down,rows):
                    temp.append(matrix[i][last_column])
                print(temp,2)  
                print(last_column,first_col)
                for i in range(last_column-1,first_col-1,-1):  
                    if last_row>start_row:
                        temp.append(matrix[last_row][i])
                print(temp,3)
                for i in range(last_row-1, start_row,-1):
                    if last_column>first_col:
                        temp.append(matrix[i][first_col])
                print(temp,4)
        
                last_column-=1
                last_row-=1
                first_col+=1
                
                first_down+=1 
                start_row+=1
                columns-=1
                rows-=1
                
            
        return temp