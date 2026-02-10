from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result=[]
        count=Counter(nums)
        for num in count:
            if count[num]>len(nums)/3:
                result.append(num)
        return result        

            
    

        