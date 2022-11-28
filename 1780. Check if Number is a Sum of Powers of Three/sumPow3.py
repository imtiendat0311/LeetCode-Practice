# Runtime: 32 ms, faster than 91.03% of Python3 online submissions for Check if Number is a Sum of Powers of Three.
# Memory Usage: 13.8 MB, less than 59.31% of Python3 online submissions for Check if Number is a Sum of Powers of Three.

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        if n ==1:
            return True
        while n > 0:
            if n % 3 == 2:
                return False
            else:
                n //= 3
        return True
