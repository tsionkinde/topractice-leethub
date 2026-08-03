class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        digitSum=0
        elementSum=sum(nums)
        for i in nums:
            for j in str(i):
                digitSum+=int(j)
        return abs(digitSum-elementSum)        
        
        