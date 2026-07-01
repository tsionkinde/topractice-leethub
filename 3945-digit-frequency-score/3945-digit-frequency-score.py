class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        total=0
        nn=str(n)
        for i in nn:
            total+=int(i)
        return total    
       
        