class Solution:
    def arraySign(self, nums: List[int]) -> int:
        neget=0
        posit=0
        zero=0
        for i in nums:
            if i>0:
                posit+=1
            elif i<0:
                neget+=1
            else:
                zero+=1
        if zero>=1:
            return 0
        elif neget%2==1:
            return -1 
        else:
            return 1              





        