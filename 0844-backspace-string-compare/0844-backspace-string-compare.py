class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack=[]
        newstack=[]
        
       
        for i in s:
            
            if i=="#":
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        for j in t:
            
            if j=="#":
                if newstack:
                    newstack.pop()
            else:
                newstack.append(j)
        if newstack==stack:
            return True
        else:
            return False                




            
         


        