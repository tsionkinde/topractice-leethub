class Solution:
    def clearDigits(self, s: str) -> str:
        stack=[]
        for i in range(len(s)):
            if  s[i].isalpha():
                stack.append(s[i])
            elif s[i].isdigit():
                if stack and not stack[-1].isdigit():
                    stack.pop() 
        return ''.join(stack)              
                

        