class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start, end = 0, 1
        while end<len(nums):
            if nums[start]==nums[end] and start!=end:
                if end==len(nums):
                    start=end
                    end+=1
                else:
                    nums[end] = "_"
                    end+=1
            else:
                start = end
                end+=1
        new_start = 0

        while new_start<len(nums):
            if nums[new_start] == "_":
                del nums[new_start]
            else:
                new_start+=1
            