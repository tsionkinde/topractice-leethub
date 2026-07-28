
class Solution:
    def maxDistinct(self, s: str) -> int:
        unique=set(s)
        count=0
        for i in unique:
            count+=1
        return count    



        