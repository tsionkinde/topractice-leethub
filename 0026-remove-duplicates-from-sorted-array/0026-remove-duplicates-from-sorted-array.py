class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow=0
        if not nums:
            return 0
        
        for fast in range  (1,len(nums)):
            if nums[slow]!=nums[fast]:
                slow+=1
                nums[slow]=nums[fast]
               
        return slow+1    #because we add 1 we start slow from 0 that is why    
          
        