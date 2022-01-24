class Solution:
    def trailingZeroes(self, n: int) -> int:
        x = 1
        prod = 1
        count = 0
        while x<=n:
            prod = prod *x
            x+=1
            
        while prod%10==0:
            count+=1
            prod = prod//10
            
        return count