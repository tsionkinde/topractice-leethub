class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        for i in edges:
            for j in i:
                if j in edges[0] and j in edges[1]:
                    return j
        return None            

                     


           
           

                
        