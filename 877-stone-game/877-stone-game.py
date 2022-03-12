class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        alice = list()
        bob = list()
        start=0
        end=len(piles)-1
        
        while start<end:
            if piles[start]>piles[end]:
                alice.append(piles[start])
                bob.append(piles[end])
            else:
                bob.append(piles[start])
                alice.append(piles[end])
            start+=1
            end-=1
        return sum(alice)>sum(bob)