from collections import Counter
class Solution:
    def topKFrequent(self,nums,k):
        count=Counter(nums)
        sorted_nums=sorted(count,key=count.get,reverse=True)
        result=[]
        
        for i in range(k):
            
            result.append(sorted_nums[i])
            
        return result        

