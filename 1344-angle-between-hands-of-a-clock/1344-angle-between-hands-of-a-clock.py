class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # hour_deg=hour(30)-minutes(6)
        
        if hour==12: 
            if minutes==0:
                hour = 0
                hour_deg=30*hour
                minute_deg=6*minutes
            else:  


                hour_deg=0
                hour=0
                hour_deg=30*hour+30/(60/minutes)
                minute_deg=6*minutes

        else:
            if minutes==0:
                hour_deg=30*hour
                minute_deg=6*minutes
            else:    
                hour_deg=30*hour+30/(60/minutes)
                minute_deg=6*minutes
        angle = abs(minute_deg - hour_deg)
        return min(angle, 360 - angle)
       



        