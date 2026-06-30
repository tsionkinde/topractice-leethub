class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        direct=0
        circular=0
        distance = float('inf')
        for i in range(len(words)):
            if words[i]==target:
                direct=abs(i-startIndex)
                circular=len(words)-direct
                distance=min(distance,min(direct,circular))
        return -1 if distance == float('inf') else distance       



    