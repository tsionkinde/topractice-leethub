class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        the_max=0
        nums.sort()
        for i in range(0,len(nums),2):
            the_max+=nums[i]
        return the_max    

       
        