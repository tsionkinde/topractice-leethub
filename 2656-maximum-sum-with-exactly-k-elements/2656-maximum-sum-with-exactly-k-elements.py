class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        score=0
        for i in range(k):
            nums.sort()
            m=nums[-1]
            nums[-1]=m+1
            score+=m
        return score    
        