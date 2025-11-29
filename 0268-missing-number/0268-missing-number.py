class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missed=0
        for i in range(min(nums),len(nums)+1):
            if i not in nums:
                missed=i
        return missed      

        