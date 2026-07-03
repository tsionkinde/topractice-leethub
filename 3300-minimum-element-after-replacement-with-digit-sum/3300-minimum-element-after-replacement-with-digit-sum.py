class Solution:
    def minElement(self, nums: List[int]) -> int:
        res=[]        
        for i in nums:
            tot=0
            for j in str(i):
                tot+=int(j)              
            res.append(tot)
        return min(res)        
             
        