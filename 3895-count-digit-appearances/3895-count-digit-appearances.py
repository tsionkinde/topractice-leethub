class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        count=0
        for i in nums:
            for j in str(i):
                if int(j)==digit:
                    count+=1
        return count            
        