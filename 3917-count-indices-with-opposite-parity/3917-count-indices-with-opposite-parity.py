class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        res=[]
        for i in range(len(nums)):
            count=0
            for j in range(i+1,len(nums)):
                if (nums[i]%2==0 and nums[j]%2==1) or (nums[i]%2==1 and nums[j]%2==0):
                    count+=1
            res.append(count)
        return res            

        