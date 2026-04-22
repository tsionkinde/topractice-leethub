from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res = []

    
        min_diff = float('inf')
        for l in range(len(arr) - 1):
            diff = arr[l+1] - arr[l]
            if diff < min_diff:
                min_diff = diff

       
        for l in range(len(arr) - 1):
            if arr[l+1] - arr[l] == min_diff:
                res.append([arr[l], arr[l+1]])

        return res 

        