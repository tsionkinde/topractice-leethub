class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        
        for num in range(left,right+1):
            covered=False
          
            for r in ranges:
                if r[0] <= num <=r[1]:
                      covered=True
                      break
            if not covered:
                return False

        return True                  

                      



        