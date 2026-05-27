from collections import Counter
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        count=Counter(nums)
        ans=-1
        freq=0    
        for i in count:
            if i%2==0:
                if count[i]>freq:
                    freq=count[i]
                    ans=i
                elif count[i]==freq:
                    ans=min(ans,i)
        return ans           


           
        