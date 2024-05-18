class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        new=[]
        a=max(candies)
        for i in range(len(candies)):
            candies[i]+=extraCandies
            if candies[i]>=a:
                new.append(True)
            else:
                new.append(False)
        return new

