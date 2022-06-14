class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        running_sum = 0
        left = 0
        best = float('inf')
        
        for right in range(n):
            running_sum += nums[right]
            
            while running_sum >= target:
                best = min(best, right - left + 1)
                running_sum -= nums[left]
                left += 1
            
        return best if best != float('inf') else 0