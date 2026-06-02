class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        minDist=float('inf')
        for i in range(len(nums)):
            if nums[i]==target:
                minDist=min( minDist,abs(i-start))
        return  minDist        

        