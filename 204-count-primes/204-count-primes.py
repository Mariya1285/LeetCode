class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=1:
            return 0
        
        primes = [True]*(n+1) # assuming all numbers are prime
        
        primes[0]=primes[1]=False # discarding 0 and 1
        
        count=0
        
        for i in range(2,n):
            if primes[i]:
                count+=1
                
                # discarding the numbers which come in table of i
                for j in range(2*i,n,i):
                    primes[j]=False
        
        return count