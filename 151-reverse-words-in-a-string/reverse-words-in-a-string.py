class Solution:
    def reverseWords(self, s: str) -> str:
        x = s.split()
        new=""
        for i in range(len(x)-1,0,-1):
            new+=x[i]+" "
        new+=x[0]
        return new
 