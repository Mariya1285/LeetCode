class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        new_str = re.sub('[a-z]', ' ', word)
        x= [int(x.strip()) for x in new_str.split(' ') if len(x)!=0]
        return len(set(x))