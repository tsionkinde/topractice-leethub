class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        themax=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                prod=(nums[i]-1)*(nums[j]-1)
                themax=max(prod,themax)
        return themax        
        