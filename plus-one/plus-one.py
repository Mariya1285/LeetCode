class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1]<9:
            digits[-1] = digits[-1]+1 
            return digits
        else:
            return str(int("".join([str(x) for x in digits]))+1)
                
                
        