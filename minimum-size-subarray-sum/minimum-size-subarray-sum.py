class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        best = float('inf')
        target_sum = 0
        left = 0
        
        for right in range(len(nums)):
            target_sum += nums[right]
            while target_sum>=target:
                best = min(best, right+1 - left)
                target_sum-=nums[left]
                left+=1
                
        if best!=float('inf'):
            return best
        else:
            return 0