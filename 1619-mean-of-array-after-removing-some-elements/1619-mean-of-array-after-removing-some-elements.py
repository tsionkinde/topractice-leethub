class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        k=len(arr)*5//100
        trimmed=arr[k:len(arr)-k]
        return sum(trimmed)/len(trimmed)
      
        