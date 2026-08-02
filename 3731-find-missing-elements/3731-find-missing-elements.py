class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        missed=[]
        for i in range(min(nums),max(nums)+1):
            if i not in nums:
                missed.append(i)
        return missed        

        