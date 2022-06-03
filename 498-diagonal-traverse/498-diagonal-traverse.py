class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        temp = list()
        rows, columns = len(mat), len(mat[0])
        reverse = False
        for col in range(columns):
            temp_row = 0
            temp_col = col
            inner_list = list()
            while temp_col>0 and temp_row<len(mat)-1:
                inner_list.append(mat[temp_row][temp_col])
                temp_row+=1
                temp_col-=1
            inner_list.append(mat[temp_row][temp_col])
            print(reverse)
            if reverse == True:
                temp.extend(inner_list)
                reverse = False
            else:
                x = inner_list[::-1]
                temp.extend(x)               
                reverse = True
            
        for row in range(1,rows):
            temp_row = row
            temp_col = columns-1
            
            inner_list = list()
            while temp_col>0 and temp_row<len(mat)-1:
                inner_list.append(mat[temp_row][temp_col])
                temp_row+=1
                temp_col-=1
            inner_list.append(mat[temp_row][temp_col])
            
            if reverse == False:
                temp.extend(inner_list[::-1])
                reverse = True
            else:
                temp.extend(inner_list)
                reverse = False
            
            
        return temp
#         if len(mat)==1:
#             return mat[0]
#         elif len(mat[0])==1:
#             return [item for sublist in mat for item in sublist]
#         for i in range(columns):
#             if i==0:
#                 temp.append(mat[i][i])
#             elif i%2!=0:
#                 column_iter= i
#                 row_iter = i-1
#                 while row_iter<len(mat) and column_iter>=0:
#                     temp.append(mat[row_iter][column_iter])
#                     column_iter-=1
#                     row_iter+=1
#             elif i%2==0:
#                 column_iter= 0
#                 row_iter = i
#                 while column_iter<len(mat) and row_iter>=0:
#                     temp.append(mat[row_iter][column_iter])
#                     column_iter+=1
#                     row_iter-=1
#         print(temp)
#         for i in range(1,rows):
#             if i%2!=0:
#                 print("I am here")
#                 row_iter = i
#                 column_iter = len(mat[0])-1
#                 while row_iter<len(mat) and column_iter>=0:
#                     # print("row_iter: ",row_iter)
#                     print("column_iter: ", column_iter)
#                     temp.append(mat[row_iter][column_iter])
#                     column_iter-=1
#                     row_iter+=1
#                 print("temp now: ", temp)
#             else:
#                 if len(mat) == len(mat[0]):
#                     column_iter= i
#                     row_iter = len(mat)-1
#                     print(row_iter)
#                     while column_iter<len(mat) and row_iter>=0:
#                         temp.append(mat[row_iter][column_iter])
#                         column_iter+=1
#                         row_iter-=1
#                 else:
#                     column_iter = len(mat[0])
#                     row_iter = len(mat)-1
#                     print(row_iter)
#                     while column_iter<len(mat) and row_iter>=0:
#                         temp.append(mat[row_iter][column_iter])
#                         column_iter+=1
#                         row_iter-=1
                    
#         return temp
                
#         diagonals = len(mat)*2-1
#         temp.append(mat[i][i])
#         for i in range(1,diagonals-1):
            
#             temp.append(mat[i][i+1])
#             temp
#         temp.append(mat[len(mat)-1][len(mat)-1])





        
        
        
        
        