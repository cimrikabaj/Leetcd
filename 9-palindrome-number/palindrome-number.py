class Solution:
    def isPalindrome(self, x: int) -> bool:
        string=''
        ori=x
        if x>=0:
            while x!=0:
                a=x % 10
                x=int(x/10)
                string=string + str(a)
            if str(ori)==string or len(str(ori))==1:
                return True
            else:
                return False
        else:
            return False

        

            
           