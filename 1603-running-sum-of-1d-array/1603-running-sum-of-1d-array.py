class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        summed_list=[]
        temp=0
        for i in range(len(nums)):
            temp+=nums[i]
            summed_list.append(temp)
        return  summed_list    


