# Runtime: 935 ms, faster than 91.39% of Python3 online submissions for Minimum Increment to Make Array Unique.
# Memory Usage: 27.9 MB, less than 88.37% of Python3 online submissions for Minimum Increment to Make Array Unique.
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        move = need = 0
        for i in sorted(nums):
            move += max(need - i, 0)
            need = max(need + 1, i + 1)
        return move