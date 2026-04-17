from collections import Counter
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        x=len(nums)/2
        count=Counter(nums)
        for i in count:
            if count[i]==x:
                return i
        return -1        

        