class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        the_index=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                     the_index.append(i)#the 2 lines of append are in two d/t lines b.c append does not take  two arguments
                     the_index.append(j)
        return the_index
            