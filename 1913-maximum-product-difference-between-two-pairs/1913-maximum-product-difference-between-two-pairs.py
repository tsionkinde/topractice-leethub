class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        a=nums[:2]
        b=nums[n-2:]
        A=1
        for i in a:
            A*=i
        B=1    
        for j in b:
            B*=j
        res=B-A   
        return res 

