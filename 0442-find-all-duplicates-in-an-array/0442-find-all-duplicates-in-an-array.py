class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        from collections import Counter
        result=[]
        count=Counter(nums)
        for num in count:
            if count[num] >1:
                result.append(num)

        return result