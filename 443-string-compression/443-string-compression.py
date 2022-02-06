class Solution:
    def compress(self, chars: List[str]) -> int:
        l = 0
        ansIndex = 0
        n = len(chars)
        while l<n:
            j = l+1
            while j<n and chars[l] == chars[j]:
                j+=1
            
            chars[ansIndex] = chars[l]
            ansIndex+=1
            coun = str(j-l)
            if coun!="1":
                for ch in coun:
                    chars[ansIndex] = ch
                    ansIndex+=1
            
            l=j
            
        return ansIndex
                
        