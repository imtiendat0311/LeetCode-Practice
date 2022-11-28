# Runtime: 67 ms, faster than 99.31% of Python3 online submissions for Power of Three.
# Memory Usage: 13.9 MB, less than 60.11% of Python3 online submissions for Power of Three.

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return True if n>0 and 1162261467%n==0 else False