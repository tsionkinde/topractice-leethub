
class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        res=[]
        
        for mat in matrix:
            count=0
            for i in mat:
                if i==1:
                    count+=1
            res.append(count)
        return res    

        
        