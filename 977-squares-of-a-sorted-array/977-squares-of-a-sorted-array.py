class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([num**2 for num in nums])
#         i = 0
#         len_num = len(nums)
#         new = list()
#         while i<len_num and nums:
#             x = min([abs(y) for y in nums])
#             new.append(x**2)
#             if x in nums:
#                 nums.remove(x)
#             else:
#                 nums.remove(-x)
            
#         return new
        

        