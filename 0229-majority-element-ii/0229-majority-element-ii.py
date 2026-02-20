from collections import Counter 
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res=[]
        count=Counter(nums)
        for num in count:
            if count[num]>(len(nums)/3):
                res.append(num)
        return res        

        
        