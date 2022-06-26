class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not all([x!=0 for x in nums]):
            pivot, start = 0, 0
            while start<len(nums):
                if nums[start] == 0 and start!=len(nums)-1:
                    if nums[pivot] !=0:
                        pivot = start
                    start+=1
                else:
                    if nums[pivot] == 0:
                        nums[pivot] = nums[start]
                        nums[start] = 0
                        pivot=pivot+1
                    start+=1
        else:
            pass