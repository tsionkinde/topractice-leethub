class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        currentsum=sum(nums[:k])
        maxavg=currentsum/k
        for i in range(k,n):
            currentsum+=nums[i]-nums[i-k]
            avg=currentsum/k
            maxavg=max(avg,maxavg)
        return maxavg    
           

       
        



       