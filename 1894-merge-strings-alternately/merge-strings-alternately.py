class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        s=""
        while i<len(word1) or i<len(word2):
            if i>=len(word1):
                s+=word2[i:]
                break
            elif i>=len(word2):
                s+=word1[i:]
                break
            else:
                s+=word1[i]+word2[i]  
                i=i+1      
        return s    