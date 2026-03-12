class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        total=0
        extra=[]
        for i,j in costs:
            total+=i
            extra.append(j-i)
        extra.sort()    
        n=len(costs)   // 2
        for k in range(n):
            total+=extra[k]
        return total    


        

          

        