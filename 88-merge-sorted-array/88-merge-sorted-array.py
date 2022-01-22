class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
#         i = 0
#         j = 0
#         if len(nums2) == 0:
#             pass
#         else:
#             for k in range(len(nums1)):
#                 if nums1[i]<nums2[j]:
#                     if nums1[i]==0:
#                         while j<len(nums2):
#                             nums1[i]=nums2[j]
#                             i+=1
#                             j+=1
#                         break
#                     else:
#                         i+=1
#                 elif nums1[i]>nums2[j]:
#                     # temp = nums1[i]
#                     # nums1[i]=nums2[j]
#                     # nums2[j] =temp
#                     nums1.insert(i+1,nums2[j])
#                     i+=2
#                     del nums2[j]
#                 elif nums1[i] == nums2[j]:
#                     nums1.insert(i+1,nums2[j])
#                     i+=2
#                     del nums2[j]

#             if 0 in nums1:
#                 idx = nums1.index(0)
#                 for i in range(idx,len(nums1)):
#                     del nums1[i]
        
#         i = m-1
#         j = n-1
#         k = len(nums1)-1
        
#         while i>=0 and j>=0:
#             if nums2[j]>nums1[i]:
#                 nums1[k] = nums2[j]
#                 j-=1
#                 k-=1
#             else:
#                 nums1[k] = nums1[i]
#                 i-=1
#                 k-=1


        p1, p2, p3 = m - 1, n - 1, len(nums1) - 1

        while p1 >= 0 and p2 >= 0:
            if nums2[p2] > nums1[p1]:
                nums1[p3] = nums2[p2]
                p2 -= 1
            else:
                nums1[p3] = nums1[p1]
                p1 -= 1
            p3 -= 1

        nums1[:p2 + 1] = nums2[:p2 + 1]
                
            
        
                
                
                
                