class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_ele = max(nums)
        if len(nums)==1:
            return 0
        else:
            for i in nums:
                if i!=max_ele and (i*2 > max_ele):
                    return -1
            return nums.index(max_ele)  