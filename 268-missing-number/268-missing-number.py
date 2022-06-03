class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        temp = list(range(len(nums)+1))
        for n in temp:
            if n not in nums:
                return n