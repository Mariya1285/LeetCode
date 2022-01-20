class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        new = sorted(nums)
        lst = [i for i in range(len(nums)) if new[i] == target]
        return lst