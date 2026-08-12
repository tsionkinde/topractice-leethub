class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count=0
        for i in range(low,high+1):
            s=str(i)
            if len(s)%2!=0:
                continue
            mid=len(s)//2    
            left =0
            for x in s[:mid]:
                left+=int(x)
            right=0    
            for y in s[mid:]:
                right+=int(y)
            if left==right:
                count+=1  
        return count              

            
        