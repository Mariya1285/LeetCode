class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_count = dict()
        for letter in magazine:
            if letter in magazine_count:
                magazine_count[letter]+=1
            else:
                magazine_count[letter] = 1
        
        for letter in ransomNote:
            if letter not in magazine_count:
                return False
            elif magazine_count[letter] == 0:
                return False
            else:
                magazine_count[letter]-=1
        return True