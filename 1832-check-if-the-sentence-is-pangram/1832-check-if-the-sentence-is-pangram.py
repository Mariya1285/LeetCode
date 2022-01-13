import string
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        x = sorted(set(sentence))
        if string.ascii_lowercase ==('').join(x):
            return True
        else:
            return False