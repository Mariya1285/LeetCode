class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        flag = True
        ransomNote_dict = dict(Counter(ransomNote))
        magazine_dict = dict(Counter(magazine))
        for letter, count_of_letter in ransomNote_dict.items():
            if letter in magazine_dict:
                if count_of_letter>magazine_dict[letter]:
                    return False
                else:
                    pass
            else:
                return False
        return True