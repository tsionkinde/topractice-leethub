class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res=[]
        x=0
        for i in nums:
            for j in str(i):
                res.append(int(j))
        return res        

           

        