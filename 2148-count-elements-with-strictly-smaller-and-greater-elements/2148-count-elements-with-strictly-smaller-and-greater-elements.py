class Solution:
    def countElements(self, nums: List[int]) -> int:
        mx=max(nums)
        mn=min(nums)
        count=0
        for x in nums:
            if mn<x<mx:
                count+=1
        return count        
        
        