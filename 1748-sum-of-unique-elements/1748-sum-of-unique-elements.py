from collections import Counter
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        summ=0
        count=Counter(nums)
        for i in count:
            if count[i]==1:
                summ+=i
        return summ        
        