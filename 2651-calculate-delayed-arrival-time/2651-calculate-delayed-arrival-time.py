class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        hours=arrivalTime+delayedTime
        if hours<24:
            return hours
        else:
            return hours%24    
        