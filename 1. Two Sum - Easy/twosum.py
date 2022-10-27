#  Faster than 96.38% other online python3 submission
#  Use less mem than 25.92% other online python3 submission
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i in range(0,len(nums)):
            if target-nums[i] in a:
                return [a[target-nums[i]],i]
            else:
                a[nums[i]]=i