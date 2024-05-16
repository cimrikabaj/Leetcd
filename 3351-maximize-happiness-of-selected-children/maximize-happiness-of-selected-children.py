class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        max_happiness=0
        i=0
        while k > 0:
            max_happiness+=max(0,happiness[i]-i)
            k=k-1
            i=i+1
        return max_happiness


        
                