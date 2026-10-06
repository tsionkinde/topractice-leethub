class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            sorted_nums=sorted(nums)
            index=nums.index(sorted_nums[0])
            nums[index]=sorted_nums[0]*multiplier
        return nums    
           
            
        