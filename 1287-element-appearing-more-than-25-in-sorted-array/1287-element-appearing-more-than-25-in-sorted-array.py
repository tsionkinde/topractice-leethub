from collections import Counter
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count=Counter(arr)
        for i in count:
            if count[i]>0.25*len(arr):
                return i
        