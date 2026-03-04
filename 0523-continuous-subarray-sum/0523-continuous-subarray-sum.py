class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder={}
        remainder[0]=-1
        current=0
        for i in range(len(nums)):
            current+=nums[i]
            if k!=0:
                current=current%k
            if current in    remainder:
                previous= remainder[current]
                if i-previous>=2:
                    return True
            else:
                remainder[current]=i
        return False        
                        

        