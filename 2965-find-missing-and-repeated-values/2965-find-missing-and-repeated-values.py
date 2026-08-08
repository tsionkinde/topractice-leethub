from collections import Counter
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        values=[]
        for i in grid:
            for j in i:
                values.append(j)
        count=Counter(values)
        repeated=0
        missing=0
        n=len(grid)
        for x in range(1,n*n+1):
            if count[x]==2:
                repeated=x
            elif count[x]==0:
                missing=x  
        return [repeated,missing]                

                    


            


        