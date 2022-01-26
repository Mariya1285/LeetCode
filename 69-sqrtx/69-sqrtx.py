class Solution:
    def mySqrt(self, x: int) -> int:
        # main = list(range(1,x))
        start = 0
        end = x
        mid = start+end//2
        
        ans = -1
        while start<=end:
            sq = mid*mid
            if sq==x:
                return mid
            if sq<x:
                start = mid+1
            else:
                end = mid-1
            
            mid=(start+end)//2
            
        return mid
            