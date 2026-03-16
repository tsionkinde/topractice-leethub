class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        arrows=1
        
        points.sort(key=lambda x:x[1])
        arrow=points[0][1]
        for start,end in points:
            if start > arrow:
                arrows+=1
                arrow=end

            
        return arrows        


        