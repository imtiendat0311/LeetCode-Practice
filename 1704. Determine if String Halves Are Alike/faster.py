# Runtime: 26 ms, faster than 99.69% of Python3 online submissions for Determine if String Halves Are Alike.
# Memory Usage: 13.9 MB, less than 33.58% of Python3 online submissions for Determine if String Halves Are Alike.

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u']
        count = 0
        first = s[:len(s)//2].lower()
        second = s[len(s)//2:len(s)].lower()
        for i in vowels:
            count += first.count(i)-second.count(i)
        return True if count==0 else False