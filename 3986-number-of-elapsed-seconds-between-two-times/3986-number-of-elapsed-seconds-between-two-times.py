class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        hour=int(startTime[:2])
        minute=int(startTime[3:5])
        second=int(startTime[6:8])
        hourE=int(endTime[:2])
        minuteE=int(endTime[3:5])
        secondE=int(endTime[6:8])
        return (hourE*3600+minuteE*60+secondE)-(hour*3600+minute*60+second)

        