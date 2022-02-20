class Solution:
    def fib(self, n: int) -> int:
#         if n==0:
#             return 0
#         if n==1:
#             return 1
        
#         return Solution.fib(self,n-1)+Solution.fib(self,n-2)

        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            pre = 0
            post = 1
            count = 2
            while count<=n:
                
                temp=post
                post=pre+post
                pre=temp
                count+=1
            return post