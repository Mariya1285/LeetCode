class Solution:
    def addDigits(self, num: int) -> int:
        if (num//10==0): return num
        else:
            while num//10!=0:
                num = (num%10)+Solution.addDigits(self,num//10)
            return num