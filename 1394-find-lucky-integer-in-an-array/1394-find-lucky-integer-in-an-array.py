from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq=Counter(arr)
        res=-1
        for i in freq:
            if i==freq[i]:
                res=max(res,i)
        return res        


        
        