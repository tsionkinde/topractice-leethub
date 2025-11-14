class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        the_index=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                     the_index.append(i)#the 2 lines of append are in two d/t lines b.c append does not take  two arguments
                     the_index.append(j)
        return the_index
            # we can also code like this b/c the above one is by using brute force
            #hm={}
            #for i,v in enumerate(nums):
                #if hm and target -v in hm:
                    #return [hm[target-v],i]
                #hm[v]=i    
