class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==1:
            return True
        y = 1
        while y * y < num:
            y += 1
        return y * y == num