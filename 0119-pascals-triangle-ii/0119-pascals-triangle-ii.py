class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        res = []
        factor = 1
        for i in range(rowIndex + 1):
            res.append(factor)
            factor = factor * (rowIndex - i) // (i + 1)  
        return res

        