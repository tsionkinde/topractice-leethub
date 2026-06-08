class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        start = 0
        res = []

        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                if i - start >= 3:
                    res.append([start, i - 1])
                start = i

        if len(s) - start >= 3:
            res.append([start, len(s) - 1])

        return res





        