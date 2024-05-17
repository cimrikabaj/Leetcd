class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        import math

        if str1 + str2 == str2 + str1:
            s = ""
            i = 0
            d = math.gcd(len(str1), len(str2))
            while d > 0:
                if str1[i] == str2[i]:
                    s += str1[i]
                    i += 1
                    d -= 1
                else:
                    break  
        else:
            s = ""
            
        return s
