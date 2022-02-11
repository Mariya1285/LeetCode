class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        main = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        len_num1 = len(num1)-1
        len_num2 = len(num2)-1
        int_num1 = 0
        int_num2 = 0
        mul1 = len_num1
        mul2 = len_num2
        for n in num1:
            
            int_num1 += main[n]*(pow(10,mul1))
            mul1 = mul1-1
        for n in num2:
            
            int_num2 += main[n]*(pow(10,mul2))
            mul2 = mul2-1
            
        return str(int_num1*int_num2)
        
            
            