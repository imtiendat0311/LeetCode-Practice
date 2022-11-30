class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        a = set(arr)
        b = 0
        c=[]
        for i in a:
            d = arr.count(i)
            if d in c:
                return False
            c.append(d)
        return True