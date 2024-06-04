class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        y = 1
        while y * y <= x:
            y += 1
        return y - 1