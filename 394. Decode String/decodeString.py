class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i != ']':
                stack.append(i)
            else:
                char=''
                while stack[-1] != '[':
                    char = stack.pop()+char
                stack.pop()
                increment = ''
                while stack and stack[-1].isdigit():
                    increment = stack.pop()+increment
                stack.append(int(increment)*char)
        return "".join(stack)