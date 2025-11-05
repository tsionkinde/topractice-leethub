class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
       slow=0# the first unique index
       if not nums:
           return 0
       for fast in range(1,len(nums)):#making fast pointer to start from 1
            if nums[slow]!= nums[fast]:#if not equeal means still it is unique
                slow+=1#if it is unique increment slow pointer to the other nidex
                nums[slow]=nums[fast]#assigning the first unique index by the next unique
       return slow+1    # it returns the length of unique elemennt because we start slow=0 we incremetn slow by 1 to count unique element      
               
        
     


        
        