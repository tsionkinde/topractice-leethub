class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=2*nums[i]
                nums[i+1]=0
        result=[]
        for num in nums:
            if num!=0:
                result.append(num)
        zeroes=len(nums)-len(result)
        result.extend([0]*zeroes)
        return result        



        