class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        l=0
        n=len(arr)
        while l<n:       
            if arr[l]==0:
                for  j in range(n-1,l,-1):
                    arr[j]=arr[j-1]
                l+=1
            l+=1        


               
             

   
                

        """
        Do not return anything, modify arr in-place instead.

        """
        