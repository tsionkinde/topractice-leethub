class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      num_to_index={}
      for index,num in enumerate(nums):
        if target-num in num_to_index:
            return [num_to_index[target-num],index]
        num_to_index[num]=index
      return []       
            
        