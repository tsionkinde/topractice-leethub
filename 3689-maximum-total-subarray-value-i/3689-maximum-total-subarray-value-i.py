class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        x=max(nums)
        y=min(nums)     
    
        return (x-y)*k
        