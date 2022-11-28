# Runtime: 24 ms, faster than 99.48% of Python3 online submissions for Power of Four.
# Memory Usage: 13.8 MB, less than 53.17% of Python3 online submissions for Power of Four.

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and not(n & (n - 1)) and n & 1431655765 == n