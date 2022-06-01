class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        for i in range(len(nums)):
            left_sum = sum(nums[:i])
            if left_sum==total_sum - sum(nums[:i+1]):
                return i
        return -1