class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest=0
        altitude=0
        for g in gain:
            altitude+=g
            highest=max(highest, altitude)
        return highest    

            
              
        