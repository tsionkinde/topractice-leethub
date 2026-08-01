class Solution:
    def pivotInteger(self, n: int) -> int:
        for x in range(n+1):
            if x/2*(1+x)==(n-x+1)/2*(x+n):
                return x
        return -1 
        
        