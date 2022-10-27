# faster than 82.44% other online python3 submission
# use less mem than 96.55% other online python3 submission
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = ""
        for i in digits:
            a = a + str(i)
        b = str(int(a)+1)  
        d = []
        for i in b:
            d.append(int(i))
        return d