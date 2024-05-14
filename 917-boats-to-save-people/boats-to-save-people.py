class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boat=0
        people.sort()
        i=0
        j=len(people)-1
        while i <= j:
            if people[i]+people[j]<=limit:
                boat=boat+1
                i=i+1
                j=j-1
            else:
                boat=boat+1
                j=j-1
        return boat

