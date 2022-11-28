# Runtime: 689 ms, faster than 90.52% of Python3 online submissions for Partition Equal Subset Sum.
# Memory Usage: 15.6 MB, less than 60.82% of Python3 online submissions for Partition Equal Subset Sum.

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        a = sum(nums)
        d = a//2
        if a %2 !=0:
            return False
        else:
            b = set()
            b.add(0)
            for i in nums:
                c=set()
                for j in b:
                    if j == d or j+i == d:
                        return True
                    c.add(j)
                    c.add(j+i)
                b = c
            return False