# Faster than 93.23% online python3 submission
# Use Less Mem than 56.77% online python3 submission

class Solution:
    def mySqrt(self, x: int) -> int:
        a, b = 0, x
        while a < b:
            mid = (a + b) // 2
            val = mid * mid
            if val == x:
                return mid
            elif val > x:
                b = mid
            else:
                a = mid + 1
        return a - 1 if a * a > x else a