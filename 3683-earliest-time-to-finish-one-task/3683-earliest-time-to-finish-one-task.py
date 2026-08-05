class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        the_min=sum(tasks[0])
        for i in tasks:
            if sum(i)<the_min:
                the_min=sum(i)
        return the_min    
                    
        