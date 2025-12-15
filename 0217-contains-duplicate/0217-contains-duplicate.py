class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
     tobe_set=len(set(nums))
     nums=len(nums)
     if  tobe_set!= nums:
        return True
     elif  tobe_set==nums:
        return False    