class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a),len(b))
        summ = list()
        carry = 0
        print(max_len)
        a = a[::-1]
        b = b[::-1]

        for i in range(max_len):
            print("carry: ", carry)
            try:
                temp_a = int(a[i])
                
            except:
                temp_a = 0
                
            try:
                temp_b = int(b[i])
            except:
                temp_b = 0
                
            print("a: ", temp_a)
            print("b: ", temp_b)
            if temp_a ==1 and temp_b ==1:
                print("11 case")
                # if i!=max_len-1:
                summ.append(0 + carry)
                carry = 1
                
            elif (temp_a == 0 or temp_b == 0) and (temp_a == 1 or temp_b == 1):
                
                if carry == 0:
                    summ.append(1)
                    carry = 0
                else:
                    summ.append(0)
                    carry = 1
            elif temp_a==0 and temp_b ==0:
                if max_len!=1:
                    summ.append(0+carry)
                else:
                    summ.append(0)
                carry = 0
            print("sum: ",summ)
            
        if max_len==1 and (a!="0" and b!="0"):
            print("last carry append")
            print(summ)
            summ.append(carry)
            print(summ)
        elif max_len!=1 and carry ==1:
            print(summ)
            summ.append(carry)
            print(summ)
        return ("").join(str(x) for x in summ[::-1])
                