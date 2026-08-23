class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        res=[]
        
        for i in range(len(nums)):
            summ=0
            for digit in str(nums[i]):
                summ+=int(str(digit))
            if summ==i:
                res.append(i)
        if not res:
            return -1
        return min(res)               

                  
        