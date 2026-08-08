from collections import Counter
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res=[]
        count=Counter(nums)
        for i in count:
            if count[i]==2:
                res.append(i)
        return res        
        