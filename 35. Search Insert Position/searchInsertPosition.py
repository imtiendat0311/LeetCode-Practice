# Faster than 86.04%
# less mem than 82.53%
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]: return 0
        for i in range(0,len(nums)):
            if (nums[i] >= target):
                return i
            if (i == len(nums)-1):
                return i+1