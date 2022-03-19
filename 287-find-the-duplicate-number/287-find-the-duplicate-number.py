class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l = [0]*(len(nums)+1)
        for i in nums:
            l[i-1]+=1
        return [l.index(l1)+1 for l1 in l if l1>1][0]
