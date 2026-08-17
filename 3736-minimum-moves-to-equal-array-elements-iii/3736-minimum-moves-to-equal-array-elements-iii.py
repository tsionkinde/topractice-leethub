class Solution:
    def minMoves(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            count+=(max(nums)-i)
        return  count    
        