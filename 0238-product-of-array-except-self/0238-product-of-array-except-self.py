class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            left = []
            product = 1
            for ele in nums:
                left.append(product)
                product = ele * product
            print(left)
            right = []
            product = 1
            for ele in nums[::-1]:
                right.append(product)
                product = ele * product
            right.reverse()
            print(right)
            output = []
            for a, b in zip(left, right):
                output.append(a*b)
            return output
