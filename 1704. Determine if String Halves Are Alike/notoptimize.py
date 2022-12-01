class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        count = 0
        for i in range(0,len(s)//2):
            if s[i] in vowels:
                count +=1
            if s[(len(s)//2)+i] in vowels:
                count -=1
        return True if count ==0 else False