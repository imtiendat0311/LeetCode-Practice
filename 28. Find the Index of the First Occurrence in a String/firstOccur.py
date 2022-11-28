# Runtime: 32 ms, faster than 93.01% of Python3 online submissions for Find the Index of the First Occurrence in a String.
# Memory Usage: 13.9 MB, less than 66.23% of Python3 online submissions for Find the Index of the First Occurrence in a String.
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            if len(haystack) == 1:
                return 0
            a=float("inf")
            for i in range(0,len(haystack)//2):
                if haystack[i:len(needle)+i] == needle and a>i:
                    return i
                if haystack[(len(haystack)-i-len(needle)):(len(haystack)-i)] == needle and a>len(haystack)-i-1:
                    a= len(haystack)-len(needle)-i
            return a
        else:
            return -1