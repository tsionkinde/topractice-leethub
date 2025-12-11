class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        w=0 # write pointer
        last=-1 
        freq=0
        for r in range(len(nums)):
            
            if nums[r]==last:               
                freq+=1
            else:
                last=nums[r]
                freq=1
            if freq<=2:
                nums[w]=nums[r]
                w+=1
        return w                
              
              
        