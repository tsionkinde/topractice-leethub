class Solution:
    def reverse(self, x: int) -> int:   

        result=str(x)[::-1]
        if x<0:
            result=result[:-1]
            result = -1*int(result)
        else:
            result = int(result)     
        if int(result)>(2**31)-1 or int(result)<-2**31 :
            return 0    
        return result    
          
        
        


        