class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n=len(arr)
        total=0
        for length in range(1,n+1,2):
            for i in range(n-length+1):
                total+=sum(arr[i:i+length])
        return total        
        