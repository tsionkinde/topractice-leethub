class Solution:
    def check(self, nums: List[int]) -> bool:
        count_breaks=0
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                count_breaks+=1
        if nums[-1]>nums[0]:
            count_breaks+=1
        return  count_breaks<=1    



        