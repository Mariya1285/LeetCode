class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        root_rotation = k%len(nums)
        print(len(nums)-root_rotation)
        temp = nums[:len(nums)-root_rotation]
        # for i in range(len(nums)-root_rotation):
        #     del nums[i]
        del nums[:len(nums)-root_rotation]
        # print(nums)
        # nums = nums[len(nums)-root_rotation:]
        print(nums)
        nums.extend(temp)
        print(nums)