class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_len = 0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            else:
                if count>max_len:
                    max_len = count
                count = 0
        if count>max_len:
            max_len = count
        return max_len