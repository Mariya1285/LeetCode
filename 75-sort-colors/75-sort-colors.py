class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1):
            min_ind = i
            for j in range(i+1,len(nums)):
                if nums[min_ind] >nums[j]:
                    temp = nums[j]
                    nums[j] = nums[min_ind]
                    nums[min_ind] = temp
                else:
                    pass
                
            
                    