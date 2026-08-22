from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count=Counter(nums)
        the_max=max(count.values())
        res=0
        for i in count.values():
            if i==the_max:
                res+=the_max
        return res            

        