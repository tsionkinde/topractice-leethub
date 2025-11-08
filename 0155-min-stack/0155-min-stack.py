class MinStack:

    def __init__(self):
        self.MinStack=[]        

    def push(self, val: int) -> None:
        self.MinStack.append(val)        

    def pop(self) -> None:
        if len(self.MinStack)==0:
            return "The stack is empty"
        return self.MinStack.pop()     

        

    def top(self) -> int:
        if len(self.MinStack)==0:
            return "The stack is empty"
        return self.MinStack[-1]    
        

    def getMin(self) -> int:
        if len(self.MinStack)==0:
            return "The stack is empty"
        return min(self.MinStack)

           

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()