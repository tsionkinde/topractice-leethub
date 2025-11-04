class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num%3!=0:#x-1+x+x+1=3x=num->x=num//3
            return []#represents there is 3 no consecutive element that sum gives equal num
        x=num//3
        return [x-1,x,x+1]
      
      
           
       



        