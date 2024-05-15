class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        a=0
        piles.sort(reverse=True)
        b=len(piles)/3
        i=0
        while b>0: 
            a+=piles[i+1] 
            b=b-1 
            i=i+2
        return a
