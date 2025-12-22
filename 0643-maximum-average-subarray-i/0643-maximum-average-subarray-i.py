class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum=0
        for i in range(k):
             current_sum+=nums[i]

        maxAvg=current_sum/k
        for i in range(k,len(nums)):
            current_sum+=nums[i]-nums[i-k]
            maxAvg=max(current_sum/k, maxAvg)
        return maxAvg    
        