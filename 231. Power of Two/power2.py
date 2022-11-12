#  faster than 96.02% of Python3 online submissions
# less than 53.65% of Python3 online submissions for Power of Two.
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        return n>0 and (n&n-1)==0