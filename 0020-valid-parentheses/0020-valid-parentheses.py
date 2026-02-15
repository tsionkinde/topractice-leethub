class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # Initialize a stack using a list
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)  # Push the opening bracket onto the stack
            else:
                # Check if the stack is empty or if the top of the stack does not match the closing bracket
                if (not stack or 
                    (c == ')' and stack[-1] != '(') or 
                    (c == '}' and stack[-1] != '{') or 
                    (c == ']' and stack[-1] != '[')):
                    return False  # Return False if brackets don't match
                stack.pop()  # Pop the top element from the stack if it matches
        
        return not stack  # Return True if the stack is empty, otherwise False
        
        