class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        if len(nums)==1:
            if nums[0]=="1":
                return str(0)
            else:
                return str(1)
        else:
            
            max_num = 2**n
            temp_str = "{0:0"+str(n)+"b}"
            binary_list = [temp_str.format(x) for x in list(range(1, max_num))]
            for any_num in binary_list:
                if any_num not in nums:
                    return any_num