class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res=[]
        the_max=max(candies)        
        
        for i in candies:           
          
            if  extraCandies + i >=the_max:
                res.append(True)
            else:
                res.append(False)
        return res        


        