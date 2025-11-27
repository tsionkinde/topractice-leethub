class Solution:
    def average(self, salary: List[int]) -> float:
        the_max=max(salary)
        the_min=min(salary)
        salary.remove(the_max)
        salary.remove(the_min)
        average=sum(salary)/len(salary)
        return average    
        