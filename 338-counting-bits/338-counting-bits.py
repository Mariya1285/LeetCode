class Solution:
    def countBits(self, n: int) -> List[int]:
        main_list = [0]
        for j in range(1,n+1):
            answer = 0
            i=0
            while j!=0:
                bit = j&1
                j = j>>1
                answer = bit*pow(10,i)+answer
                i+=1

            main_list.append(str(answer).count('1'))
        return main_list