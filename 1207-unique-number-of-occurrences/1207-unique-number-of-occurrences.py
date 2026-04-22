from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count=Counter(arr)
        res=[]
        for i in count:
            res.append(count[i])
        if len(res)==len(set(res)):
            return True
        else:
            return False        

        