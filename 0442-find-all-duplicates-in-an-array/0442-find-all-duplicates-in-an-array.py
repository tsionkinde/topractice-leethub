class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        indexes={}
        result=[]
        for num in nums:
            if num in indexes:
                indexes[num]+=1
            else:
                indexes[num]=1
        for num in indexes:
            if indexes[num]>1:
                result.append(num)
        return result                    
        