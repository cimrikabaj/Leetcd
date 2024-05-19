class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        for i in range(length):
            if flowerbed[i] == 0:
                # Check if the left and right plots are empty or out of bounds
                empty_left = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right = (i == length - 1) or (flowerbed[i + 1] == 0)
                if empty_left and empty_right:
                    # Plant a flower here
                    flowerbed[i] = 1
                    n -= 1
                    if n == 0:
                        return True
        return n <= 0